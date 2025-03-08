from sqlmodel import SQLModel, Field
from typing import Optional

class Coach(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    specialization: str  # Chuyên môn (cờ tàn, khai cuộc, chiến thuật)
    phone: str
    email: str
    profile_picture: Optional[str] = None  # URL ảnh đại diện
