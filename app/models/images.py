from db.base_class import Base
from sqlalchemy import Column, Datetime, Float, Integer, String
from sqlalchemy.orm import relationship


class Image(Base):
    id = Column(Integer, primary_key=True)
    action = Column(String)
    url_original_file = Column(String)
    url_new_file = Column(Integer)
    image_name = Column(Float)
    created_at = Column(Datetime)
    user = relationship("User", back_populates="user")