from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    date_of_birth: date
    age: int
    gender: str
    phone: str
    email: str
    address: str
    profile_picture: Optional[str] = None  # URL ảnh đại diện

    # Thông tin trình độ
    elo_current: int = Field(default=250)  # ELO hiện tại
    elo_classical: int = Field(default=250)
    elo_rapid: int = Field(default=250)
    elo_blitz: int = Field(default=250)
    
    completed_skills: Optional[str] = None  # Danh sách kỹ năng hoàn thiện (JSON hoặc text)
