from middlewares.error_handler import ErrorHandler
from core.config import settings
from db.base_class import Base
from db.session import engine
from fastapi import FastAPI


def create_tables():         
	Base.metadata.create_all(bind=engine)
        

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    create_tables()
    return app


app = start_application()
app.add_middleware(ErrorHandler)


@app.get("/", tags=['home'])
def read_root():
    return {"Hello": "World"}