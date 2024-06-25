

from typing import List

from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from config import Base

class ScanResult(Base):
    """
    A class representing the result of a scan.

    Attributes:
        - Id (int): The unique identifier for the scan result.
        - Result (str): The result of the scan, stored as a string.
        - ScanId (int): The ID of the scan to which this result belongs.
        - Scan (Scan): The relationship to the Scan object that this result is associated with.
    """

    __tablename__ = "ScanResult"

    Id:             Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    Description:    Mapped[str] = mapped_column(String(1000), nullable=False)

    Url:            Mapped[str] = mapped_column(String(200), nullable=False) 
    Risk:           Mapped[str] = mapped_column(String(50), nullable=False)

    ScanId:         Mapped[int] = mapped_column(ForeignKey("Scan.Id"))
    Scan:           Mapped['Scan'] = relationship(back_populates='Result')