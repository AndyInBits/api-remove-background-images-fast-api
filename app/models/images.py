from db.base_class import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Image(Base):
    id = Column(Integer, primary_key=True)
    url_new_file = Column(String)
    created_at = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="images")