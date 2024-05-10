from sqlalchemy import Integer, String, ForeignKey, Column, Boolean
from db.base_class import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column





class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    email: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(500))
    is_superuser: Mapped[bool] = Column(Boolean)
    is_active: Mapped[bool] = Column(Boolean)