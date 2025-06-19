    

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    vision = Column(String)
    skills = Column(String)
    mindset = Column(String)
    hours = Column(Integer)
    risk = Column(String)
    embedding = Column(String)  # ✅ THIS LINE MUST BE PRESENT

engine = create_engine('sqlite:///successsync.db')
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()
