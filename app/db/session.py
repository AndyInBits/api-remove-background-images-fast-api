from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

database_url = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_SERVER}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"

engine = create_engine(database_url, echo=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
