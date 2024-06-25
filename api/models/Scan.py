import datetime

from typing import List

from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from models.ScanResult import ScanResult
from config import Base

class Scan(Base):
    """
    The Scan class represents a table in the database that stores information about scans.

    Attributes:
        - Id (int): The primary key of the Scan table, auto-incremented.
        - Type (str): The type of scan, cannot be nullable.
        - ApplicationName (str): The name of the application being scanned, cannot be nullable.
        - StartAt (datetime.datetime): The start time of the scan, cannot be nullable.
        - Status (int): The status of the scan, represented as an integer, cannot be nullable.
        - Urls (List[ApplicationUrl]): The list of application URLs associated with this scan, establishing a relationship with the ApplicationUrl table.
    """
    
    __tablename__ = "Scan"

    Id:                 Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Type:               Mapped[str] = mapped_column(String(20), nullable=False)
    ApplicationName:    Mapped[str] = mapped_column(String(100), nullable=False)
    StartAt:            Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
    Status:             Mapped[int] = mapped_column(Integer, nullable=False)

    Urls:               Mapped[List["ApplicationUrl"]] = relationship(back_populates="Scan")
    Result:             Mapped[List["ScanResult"]] = relationship(back_populates="Scan")