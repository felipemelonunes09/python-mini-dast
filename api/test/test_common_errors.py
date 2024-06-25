import unittest
from unittest.mock import patch

from shared.errors.commom import InvalidAtributesError, RegistryNotFound, RequestMustBeJsonError, ScanStatusUpdateError

class TestErrors(unittest.TestCase):

    def test_request_must_be_json_error(self):
        error = RequestMustBeJsonError()
        self.assertEqual(error.status_code, 400)
        self.assertEqual(error.message, "The request payload must be in json format")
        self.assertIsNone(error.payload)

    def test_invalid_attributes_error(self):
        error = InvalidAtributesError()
        self.assertEqual(error.status_code, 400)
        self.assertEqual(error.message, "One or more atributes is invalid")
        self.assertIsNone(error.payload)

    def test_scan_status_update_error(self):
        error = ScanStatusUpdateError()
        self.assertEqual(error.status_code, 400)
        self.assertEqual(error.message, "Error when updating scan status")
        self.assertIsNone(error.payload)

    def test_registry_not_found_error(self):
        error = RegistryNotFound()
        self.assertEqual(error.status_code, 404)
        self.assertEqual(error.message, "Registry not found")
        self.assertIsNone(error.payload)
