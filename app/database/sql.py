from sqlalchemy import String, DateTime, Column, Boolean
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:admin@localhost:5432/postgres")
BaseModel = declarative_base()
Session = sessionmaker(bind=engine)


class UserModel(BaseModel):
    __tablename__ = 'users'
    username = Column(String(50), primary_key=True, nullable=False)
    passwd = Column(String(100), nullable=False)
    name = Column(String(256), nullable=False)
    email = Column(String(256), nullable=False)
    admin = Column(Boolean, default=False, nullable=False)

BaseModel.metadata.create_all(bind=engine)