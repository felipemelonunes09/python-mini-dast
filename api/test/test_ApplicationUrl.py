import unittest
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.ApplicationUrl import ApplicationUrl
from models.Scan import Scan

from config import Base

class TestApplicationUrl(unittest.TestCase):

    def setUp(self):
        # Set up an in-memory SQLite database
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.session_factory = sessionmaker(bind=self.engine)
        self.Session = scoped_session(self.session_factory)
        self.session = self.Session()

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)
        self.engine.dispose()

    def test_create_application_url(self):
        # Create a Scan instance
        scan = Scan(
            Type=0,
            ApplicationName="Scan",
            StartAt=datetime.datetime.now(),
            Status=1
        )
        self.session.add(scan)
        self.session.commit()

        # Create an ApplicationUrl instance
        app_url = ApplicationUrl(Name="Test Application", Url="http://example.com", ScanId=scan.Id)
        self.session.add(app_url)
        self.session.commit()

        # Query the ApplicationUrl instance
        retrieved_app_url = self.session.query(ApplicationUrl).first()
        self.assertIsNotNone(retrieved_app_url)
        self.assertEqual(retrieved_app_url.Name, "Test Application")
        self.assertEqual(retrieved_app_url.Url, "http://example.com")
        self.assertEqual(retrieved_app_url.ScanId, scan.Id)

    def test_relationship_with_scan(self):
        # Create a Scan instance
        scan = Scan(
            Type=0,
            ApplicationName="Scan",
            StartAt=datetime.datetime.now(),
            Status=1
        )
        self.session.add(scan)
        self.session.commit()

        # Create an ApplicationUrl instance
        app_url = ApplicationUrl(Name="Test Application", Url="http://example.com", ScanId=scan.Id)
        self.session.add(app_url)
        self.session.commit()

        # Check the relationship
        self.assertEqual(app_url.Scan.Id, scan.Id)
        self.assertEqual(scan.Urls[0].Name, "Test Application")

