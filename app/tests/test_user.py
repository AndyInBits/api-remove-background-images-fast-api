


from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.base_class import Base
from routes.user import user_router
from main import app
from db.session import Session
from sqlalchemy.pool import StaticPool


SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool,
)


TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.rollback()
        db.close()

app.dependency_overrides[Session] = override_get_db

client = TestClient(app)

def test_create_user_endpoint():
    assert client is not None
    user_data = {
        "email": "test@example.com",
        "password": "TestPassword",
        "password_confirmation": "TestPassword",
        "full_name": "Test User"
    }
    response = client.post("/users", json=user_data)
    assert response.status_code == 200
    assert response.json()["email"] == user_data["email"]
    assert "token" in response.json()

def test_create_user_non_matching_password_endpoint():
    user_data = {
        "email": "test@example.com",
        "password": "TestPassword",
        "password_confirmation": "DifferentPassword",
        "full_name": "Test User"
    }
    response = client.post("/users", json=user_data)
    assert response.status_code == 422
    assert "Password confirmation does not match password" in response.text
