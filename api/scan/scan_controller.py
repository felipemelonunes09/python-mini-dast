from flask import Blueprint, request

from scan.scan_service import ScanService
from shared.Singleton import SingletonMeta
from shared.errors.commom import InvalidAtributesError, RequestMustBeJsonError

from config import db_instance

scan = Blueprint('scan', __name__)
scan_service = ScanService(instance=db_instance)

class ScanController(metaclass=SingletonMeta):
        
    @scan.route("/", methods=["POST"])
    def create():
        """
        Create a new scan.

        Request Body JSON Format:
        {
            "application_name": "string",
            "start_at": "string",
            "urls": ["string"]
        }

        Returns:
            - dict: A message indicating whether the scan was created successfully or not.

        Raises:
            - RequestMustBeJsonError: If the request is not in JSON format.
        """
        
        if not request.is_json:
            raise RequestMustBeJsonError()
        
        data = request.json
        scan =  {
            "type":            "DAST",
            "status":           ScanService.scan_status['Created'],
            "application_name": data.get("application_name"),
            "start_at":         data.get("start_at")
        }        

        urls = data.get("urls", None)

        created = scan_service.create(scan, urls)
        if created:
            return { "message": "Registry created" },201 
        else:
            return { "message": "Registry could not be created" }, 500

    @scan.route("/<int:id>/status", methods=["GET"])
    def get_status(id):
        """
        Get the status of a scan by its ID.

        Args:
            - id (int): The ID of the scan.

        Returns:
            - dict: A message containing the status of the scan.
        """

        scan_status = scan_service.get_status(id)
        return ({ "response": scan_status }, 200)
    
    @scan.route("/<int:id>/update-status", methods=["POST"])
    def update_status(id):
        """
        Update the status of a scan.

        Request Body JSON Format:
        {
            "error_ocurred": "boolean"
        }

        Returns:
            - dict: A message indicating whether the status was updated successfully or not.

        Raises:
            - RequestMustBeJsonError: If the request is not in JSON format.
        """

        if not request.is_json:
            raise RequestMustBeJsonError()
        
        data = request.json
        status =  {
            "error_ocurred": data.get("error_ocurred")
        }  

        updated = scan_service.update_status(id, status)
        if updated:
            return { "message": "status updated" }, 200
        
        return { "message": "Registry could not be updated" }, 500

    
    @scan.route("/unprocessed-scans", methods=["GET"])
    def get_unprocessed_scans():
        """
        Get a list of unprocessed scans.

        Returns:
            - dict: A message containing the list of unprocessed scans.
        """

        scans = scan_service.get_unprocessed_scans()
        return ({"response": scans }, 200)
    
    @scan.route("/<int:id>/result", methods=['POST'])
    def create_result(id):
        """
        Create a result for a scan.

        Request Body JSON Format:
        {
            "result": "string"
        }

        Returns:
            - dict: A message indicating whether the result was created successfully or not.

        Raises:
            - RequestMustBeJsonError: If the request is not in JSON format.
        """
        
        if not request.is_json:
            raise RequestMustBeJsonError()
        
        data = request.json
        data =  {"result": data.get("result", None)}

        created = scan_service.create_result(id, data)  
        if created:
            return { "message": "Registry created" }, 201 
        else:
            return { "message": "Registry could not be created" }, 500
        

    @scan.route("/<int:id>/result", methods=["GET"])
    def get_result(id):
        """
        Get the result of a scan by its ID.

        Args:
            - id (int): The ID of the scan.

        Returns:
            - dict: A message containing the result of the scan.
        """
        result = scan_service.get_result_by_scan_id(id)
        return ({ "response": result }, 200) 