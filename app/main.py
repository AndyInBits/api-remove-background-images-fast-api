from core.config import settings
from db.base_class import Base
from db.session import engine
from fastapi import FastAPI
from middlewares.error_handler import ErrorHandler
from routes.healcheck import healcheck_router
from routes.image import images_router
from routes.user import user_router


def create_tables():         
	Base.metadata.create_all(bind=engine)
        

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    create_tables()
    return app


app = start_application()
app.add_middleware(ErrorHandler)


app.include_router(healcheck_router)
app.include_router(user_router)
app.include_router(images_router)