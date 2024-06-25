import unittest
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from config import Base
from models.Scan import Scan
from models.ApplicationUrl import ApplicationUrl

class TestScan(unittest.TestCase):

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

    def test_create_scan(self):
        start_time = datetime.datetime.now()
        scan = Scan(Type="Full", ApplicationName="Test Application", StartAt=start_time, Status=1)
        self.session.add(scan)
        self.session.commit()

        # Query the Scan instance
        retrieved_scan = self.session.query(Scan).first()
        self.assertIsNotNone(retrieved_scan)
        self.assertEqual(retrieved_scan.Type, "Full")
        self.assertEqual(retrieved_scan.ApplicationName, "Test Application")
        self.assertEqual(retrieved_scan.StartAt, start_time)
        self.assertEqual(retrieved_scan.Status, 1)

    def test_relationship_with_application_url(self):
        start_time = datetime.datetime.now()
        scan = Scan(Type="Full", ApplicationName="Test Application", StartAt=start_time, Status=1)
        self.session.add(scan)
        self.session.commit()

        app_url = ApplicationUrl(Name="Test Application URL", Url="http://example.com", ScanId=scan.Id)
        self.session.add(app_url)
        self.session.commit()

        self.assertEqual(len(scan.Urls), 1)
        self.assertEqual(scan.Urls[0].Name, "Test Application URL")
        self.assertEqual(scan.Urls[0].Url, "http://example.com")

if __name__ == '__main__':
    unittest.main()
