from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_FILE = "task_manager.db"
DATABASE_URL = f"sqlite:///{os.path.join(os.path.dirname(__file__), DATABASE_FILE)}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
