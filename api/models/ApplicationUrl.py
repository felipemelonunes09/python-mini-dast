from sqlalchemy import ForeignKey, String, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from models.Scan import Scan

from config import Base

class ApplicationUrl(Base):

    """
    The ApplicationUrl class represents a table in the database that stores information about application URLs.

    Attributes:
        - Id (int): The primary key of the ApplicationUrl table, auto-incremented.
        - Name (str): The name of the application URL, can be nullable.
        - Url (str): The URL of the application, cannot be nullable.
        - ScanId (int): The foreign key linking to the Scan table.
        - Scan (Scan): The relationship to the Scan object, indicating the Scan that this URL is associated with.
    """

    __tablename__ = "ApplicationUrl"

    Id:            Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Name:          Mapped[str] = mapped_column(String(100), nullable=True)
    Url:           Mapped[str] = mapped_column(String(255), nullable=False)

    ScanId:        Mapped[int] = mapped_column(ForeignKey("Scan.Id"))
    Scan:          Mapped["Scan"] = relationship(back_populates="Urls")