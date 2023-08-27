from sqlalchemy import Column, Float, Integer, String, Datetime
from db.base_class import Base


class Image(Base):
    id = Column(Integer, primary_key=True)
    action = Column(String)
    url_original_file = Column(String)
    url_new_file = Column(Integer)
    image_name = Column(Float)
    created_at = Column(Datetime)