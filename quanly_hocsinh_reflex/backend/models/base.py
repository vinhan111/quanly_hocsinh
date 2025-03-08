from sqlmodel import SQLModel, create_engine, Session
import os

# Định nghĩa đường dẫn database
DATABASE_URL = "sqlite:///data/database.db"
engine = create_engine(DATABASE_URL, echo=True)

# Hàm tạo bảng trong database
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Hàm lấy session để thao tác với database
def get_session():
    return Session(engine)
