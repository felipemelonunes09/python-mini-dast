
class BaseError(Exception):
    """
    Base class for custom exceptions.

    Attributes:
        - message (str): A description of the error.
        - status_code (int): The HTTP status code associated with the error.
        - payload (dict): Additional information about the error.

    Methods:
        - to_dict(): Returns a dictionary representation of the error.
    """
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):

        """
        Initialize the BaseError instance.

        Args:
            - message (str): A description of the error.
            - status_code (int): The HTTP status code associated with the error.
            - payload (dict): Additional information about the error.
        """

        Exception.__init__(self)

        if message is not None:
            self.message = message

        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        """
            Returns a dictionary representation of the error.

            Returns:
            - dict: A dictionary with the error message and any additional payload.
        """
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
    
class RequestMustBeJsonError(BaseError):
    """
        Exception raised when the request payload it's not in JSON format.
    """
    def __init__(self, message="The request payload must be in json format", payload=None):
        super().__init__(message, 400, payload)

class InvalidAtributesError(BaseError):
    """
        Exception raised when one or more attributes of the requisition are invalid..
    """
    def __init__(self, message="One or more atributes is invalid", payload=None):
        super().__init__(message, 400, payload)

class ScanStatusUpdateError(BaseError):
    """
        Exception raised when there is an error updating scan status.
    """
    def __init__(self, message="Error when updating scan status", status_code=400, payload=None):
        super().__init__(message, status_code, payload)

class RegistryNotFound(BaseError):
    """
        Exception raised when a registry is not found.
    """
    def __init__(self, message="Registry not found", payload=None):
        super().__init__(message, 404, payload)
