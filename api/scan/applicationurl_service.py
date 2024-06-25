
from models.ApplicationUrl import ApplicationUrl
from shared.errors.commom import InvalidAtributesError

class ApplicationUrlService():
    """
    A service class for creating ApplicationUrl objects.

    Attributes:
    - create_db_object: A static method to create a new ApplicationUrl object based on input data.
    """

    @staticmethod
    def create_db_object(application_url, scan_id):   
        """
        Create a new ApplicationUrl object.

        Args:
            - application_url (dict): A dictionary containing the attributes of the ApplicationUrl object.
            - scan_id (int): The ID of the scan associated with the ApplicationUrl.

        Returns:
            - ApplicationUrl: The newly created ApplicationUrl object.

        Raises:
            - InvalidAtributesError: If the application_url is not a dictionary.
        """
        
        if not isinstance(application_url, dict):
            raise InvalidAtributesError("Urls must be passed as dictionary")

        new_url = ApplicationUrl(
            Name        = application_url.get("name", None),
            Url         = application_url.get("url", None),
            ScanId      = scan_id
        )

        return new_url
