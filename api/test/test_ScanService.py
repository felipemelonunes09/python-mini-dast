import datetime
import unittest
from unittest.mock import MagicMock, patch
from shared.errors.commom import InvalidAtributesError, RegistryNotFound, ScanStatusUpdateError
from scan.scan_service import ScanService

class TestScanService(unittest.TestCase):

    def setUp(self):
        self.mock_instance = MagicMock()
        self.scan_service = ScanService(self.mock_instance)
        self.scan_service.instance = self.mock_instance


    def test_get_scan_by_id_success(self):
        mock_scan = MagicMock()
        self.mock_instance.get_session().query().get.return_value = mock_scan

        result = self.scan_service.get_scan_by_id(1)

        self.assertEqual(result, mock_scan)
        self.mock_instance.get_session().query().get.assert_called_once_with(1)

    def test_get_scan_by_id_not_found(self):
        self.mock_instance.get_session().query().get.return_value = None

        with self.assertRaises(RegistryNotFound):
            self.scan_service.get_scan_by_id(1)

    def test_get_status(self):


        mock_instance = MagicMock()
        scan_service = ScanService(instance=None)
        scan_service.instance = mock_instance

        mock_scan = MagicMock()
        mock_scan.Status = 2
        scan_service.get_scan_by_id = MagicMock(return_value=mock_scan)

        result = scan_service.get_status(1)

        self.assertEqual(result, {"status_code": 2})
        scan_service.get_scan_by_id.assert_called_once_with(1)
    
    @patch('scan.scan_service.asyncio.get_event_loop')
    async def test_create_success(self, mock_get_event_loop):

        mock_scan = {"type": "type1", "application_name": "app1", "start_at": "now", "status": 1}
        mock_urls = ["url1", "url2"]
        mock_new_scan = MagicMock()
        mock_application_url_service = MagicMock()
        mock_application_url = MagicMock()

        with patch('scan.scan_service.Scan', return_value=mock_new_scan), \
             patch('scan.scan_service.ApplicationUrlService', return_value=mock_application_url_service):
            mock_application_url_service.create.return_value = mock_application_url

            with patch('scan.scan_service.notify_scan_created', new_callable=AsyncMock) as mock_notify_scan_created:
                result = await self.scan_service.create(mock_scan, mock_urls)

                self.assertTrue(result)
                self.mock_instance.get_session().commit.assert_called()
                mock_notify_scan_created.assert_not_called()
            
    def test_create_invalid_urls(self):
        mock_scan = {"type": "type1", "application_name": "app1", "start_at": "now", "status": 1}

        with self.assertRaises(InvalidAtributesError):
            self.scan_service.create(mock_scan, None)

    def test_get_unprocessed_scans(self):
        mock_scan = MagicMock()
        mock_scan.Id = 1
        mock_scan.ApplicationName = "app1"
        mock_scan.Type = "type1"
        mock_scan.Status = 1
        mock_scan.Urls = [MagicMock(Name="name1", Url="url1")]

        self.mock_instance.get_session().query().filter().all.return_value = [mock_scan]

        result = self.scan_service.get_unprocessed_scans()

        expected_result = [{
            "id": 1,
            "application_name": "app1",
            "type": "type1",
            "status": 1,
            "urls": [{"name": "name1", "url": "url1"}]
        }]
        self.assertEqual(result, expected_result)

    def test_update_status_success(self):
        mock_scan = MagicMock()
        mock_scan.Status = 1
        self.scan_service.get_scan_by_id = MagicMock(return_value=mock_scan)

        status = {"error_ocurred": False}
        result = self.scan_service.update_status(1, status)

        self.assertTrue(result)
        self.mock_instance.get_session().commit.assert_called()
        self.scan_service.get_scan_by_id.assert_called_once_with(1)

    def test_update_status_error_occurred(self):
        mock_scan = MagicMock()
        self.scan_service.get_scan_by_id = MagicMock(return_value=mock_scan)

        status = {"error_ocurred": True}
        result = self.scan_service.update_status(1, status)

        self.assertTrue(result)
        self.mock_instance.get_session().commit.assert_called()
        self.scan_service.get_scan_by_id.assert_called_once_with(1)
        self.assertEqual(mock_scan.Status, ScanService.scan_status['Error'])
        
    def test_update_status_finished(self):
        mock_scan = MagicMock()
        mock_scan.Status = ScanService.scan_status['Finished']
        self.scan_service.get_scan_by_id = MagicMock(return_value=mock_scan)

        with self.assertRaises(ScanStatusUpdateError):
            self.scan_service.update_status(1, {"error_ocurred": False})
    
    def test_update_status_error(self):
        mock_scan = MagicMock()
        mock_scan.Status = ScanService.scan_status['Error']
        self.scan_service.get_scan_by_id = MagicMock(return_value=mock_scan)

        with self.assertRaises(ScanStatusUpdateError):
            self.scan_service.update_status(1, {"error_ocurred": False})