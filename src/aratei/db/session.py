from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.aratei.db.models.base import Base


DATABASE_URL = (
    "sqlite:///mydb.db"  # Todo create config for alchemy and move this to envfile
)

engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
