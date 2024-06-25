import asyncio

from models.Scan import Scan
from models.ScanResult import ScanResult
from scan.scan_notify import notify_scan_created

from scan.applicationurl_service import ApplicationUrlService
from shared.errors.commom import InvalidAtributesError, RegistryNotFound, ScanStatusUpdateError
from shared.Singleton import SingletonMeta

class ScanService(metaclass=SingletonMeta):

    """
    A service class for handling scan-related operations.

    Attributes:
    - scan_status (dict): A dictionary mapping scan statuses to their corresponding codes.
    - instance: The database instance used for session management.
    """
    
    scan_status = { "Created": 1, "Executing": 2 , "Error": 3, "Finished": 4} 

    def __init__(self, instance) -> None:
        """
        Initialize the ScanService with a database instance.

        Args:
            - instance: The database instance.
        """
        self.instance = instance

    def get_scan_by_id(self, id) -> Scan:
        """
        Retrieve a scan by its ID.

        Args:
            - id (int): The ID of the scan.

        Returns:
            - Scan: The scan object.

        Raises:
            - RegistryNotFound: If the scan with the given ID does not exist.
        """
        scan = self.instance.get_session().query(Scan).get(id)
        if scan:
            return scan
        raise RegistryNotFound()
    
    def get_status(self, id):
        """
        Get the status of a scan by its ID.

        Args:
            - id (int): The ID of the scan.

        Returns:
            - dict: A dictionary containing the status code of the scan.
        """
        scan = self.get_scan_by_id(id)
        return { "status_code": scan.Status }

    def create(self, scan, urls):
        """
        Create a new scan and associated URLs.

        Args:
            - scan (dict): A dictionary containing the attributes of the scan.
            - urls (list): A list of dictionaries containing URL information.

        Returns:
            - bool: True if the scan was created successfully, False otherwise.

        Raises:
            - InvalidAtributesError: If the URLs are None.
        """

        new_scan = Scan(
            Type            = scan.get("type", None),
            ApplicationName = scan.get("application_name", None),
            StartAt         = scan.get("start_at", None),
            Status          = scan.get("status", None)
        )

        if urls is None:
            raise InvalidAtributesError("urls can not be None")

        self.instance.get_session().add(new_scan)
        self.instance.get_session().commit()

        for url in urls:
            application_url = ApplicationUrlService().create_db_object(url, new_scan.Id)
            if application_url is None: return False
            self.instance.get_session().add(application_url)
            
        self.instance.get_session().commit()

        asyncio.get_event_loop().run_until_complete(notify_scan_created(new_scan))
        
        return True

    def get_unprocessed_scans(self):
        """
        Get a list of unprocessed scans.

        Returns:
            - list: A list of dictionaries containing information about unprocessed scans.
        """

        scan_list = []
        scan_objects = self.instance.get_session().query(Scan).filter(Scan.Status == ScanService.scan_status["Created"]).all()

        for scan in scan_objects:
            url_list = []
            for url in scan.Urls:
                url_list.append({
                    "name":     url.Name,
                    "url":      url.Url
                })

            scan_list.append(
                {
                    "id":               scan.Id,
                    "application_name": scan.ApplicationName,
                    "type":             scan.Type,
                    "status":           scan.Status,
                    "urls":             url_list
                })
            
        return scan_list

    
    def update_status(self, id, status):

        """
        Update the status of a scan by its ID.

        Args:
            - id (int): The ID of the scan.
            - status (dict): A dictionary containing the new status information.

        Returns:
            - bool: True if the status was updated successfully, False otherwise.

        Raises:
            - ScanStatusUpdateError: If the scan is already finished or in error state.
        """
        
        error_ocurred = status.get("error_ocurred", False)
        scan = self.get_scan_by_id(id)

        if scan.Status == ScanService.scan_status['Finished']:
            raise ScanStatusUpdateError("This scan can not be changed because it is already finished")
        
        if scan.Status == ScanService.scan_status['Error']:
            raise ScanStatusUpdateError("This scan can not be changed because the scan failed")

        if error_ocurred:
            scan.Status = ScanService.scan_status['Error']
            self.instance.get_session().commit()
            return True

        if scan.Status == ScanService.scan_status['Created']:
            scan.Status = ScanService.scan_status['Executing']
        elif scan.Status == ScanService.scan_status['Executing']:
            scan.Status = ScanService.scan_status['Finished']

        self.instance.get_session().commit()
        return True


    def create_result(self, scan_id, data):
        """
        Create a result for a scan by its ID.

        Args:
            - scan_id (int): The ID of the scan.
            - data (dict): A dictionary containing the result data.

        Returns:
            - bool: True if the result was created successfully, False otherwise.

        Raises:
            - InvalidAtributesError: If the scan is already finished.
        """
        
        scan = self.get_scan_by_id(scan_id)

        if scan.Status == ScanService.scan_status['Finished']:
            raise InvalidAtributesError("You can't add a result to a finished scan")

        result = ScanResult(
            Result = data.get('result', None),
            ScanId = scan.Id
        )

        self.instance.get_session().add(result)
        self.instance.get_session().commit()

        return True
    
    def get_result_by_scan_id(self, id: int) -> dict:
        """
        Get the result of a scan by its ID.

        Args:
            - id (int): The ID of the scan.

        Returns:
            - dict: A dictionary containing the result of the scan.

        Raises:
            - RegistryNotFound: If the result is not found.
        """

        scan = self.get_scan_by_id(id)
        
        results_objects = self.instance.get_session().query(ScanResult).filter( ScanResult.ScanId == id ).all()
        if results_objects == None:
            return RegistryNotFound()
        
        results = []
        for obj in results_objects:
            results.append({
                "scan_id": obj.ScanId,
                "result": obj.Result
            })

        return {"results": results}