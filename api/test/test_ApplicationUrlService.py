import unittest
from unittest.mock import patch
from models.ApplicationUrl import ApplicationUrl
from shared.errors.commom import InvalidAtributesError
from scan.scan_service import ApplicationUrlService

class TestApplicationUrlService(unittest.TestCase):

    def setUp(self):
        self.valid_application_url = {
            "name": "Example",
            "url": "http://example.com"
        }
        self.invalid_application_url = ["invalid", "data"]
        self.scan_id = 1

    def test_create_db_object_success(self):
        new_url = ApplicationUrlService.create_db_object(self.valid_application_url, self.scan_id)
        
        self.assertIsInstance(new_url, ApplicationUrl)
        self.assertEqual(new_url.Name, self.valid_application_url["name"])
        self.assertEqual(new_url.Url, self.valid_application_url["url"])
        self.assertEqual(new_url.ScanId, self.scan_id)

    def test_create_db_object_invalid_attributes(self):
        with self.assertRaises(InvalidAtributesError):
            ApplicationUrlService.create_db_object(self.invalid_application_url, self.scan_id)

