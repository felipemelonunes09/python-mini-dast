import datetime
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from models.Scan import Scan
from models.ScanResult import ScanResult

from config import Base

# Define your test class
class TestScanResult(unittest.TestCase):

    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.session_factory = sessionmaker(bind=self.engine)
        self.Session = scoped_session(self.session_factory)
        self.session = self.Session()

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)
        self.engine.dispose()

    def test_scan_result_creation(self):

        scan = Scan(Type="Full", ApplicationName="Test Application", StartAt=datetime.datetime.now(), Status=1)
        self.session.add(scan)
        self.session.commit()

        scan_result = ScanResult(
            Description="Some result", 
            Url="/url",
            Risk="Medium", 
            ScanId=scan.Id
            )
        self.session.add(scan_result)
        self.session.commit()

        result_from_db = self.session.query(ScanResult).filter_by(Id=scan_result.Id).one()
        self.assertEqual(result_from_db.ScanId, scan.Id)

