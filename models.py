from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class GroupClasses(Base):
    __tablename__= "group_classes"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name_course: Mapped[str] = mapped_column(String(100), nullable=False)
    name_coach: Mapped[str] = mapped_column(String(100), nullable=False)
    capacity_of_participants: Mapped[int] = mapped_column(nullable=False, default=0)
    price: Mapped[int] = mapped_column(nullable=False, default=0)
    