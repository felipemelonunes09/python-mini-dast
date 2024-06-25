from flask import jsonify
from run import app
from config import db_instance as instance 

from shared.errors.commom import RegistryNotFound, RequestMustBeJsonError, InvalidAtributesError, ScanStatusUpdateError
from sqlalchemy.exc import IntegrityError, OperationalError

def common_handler(error):
    instance.session.rollback()
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.errorhandler(RequestMustBeJsonError)
def handle_must_be_json(error):
    return common_handler(error)

@app.errorhandler(InvalidAtributesError)
def handle_invalid_atributes(error):
    return common_handler(error)

@app.errorhandler(RegistryNotFound)
def handle_registry_not_found(error):
    return common_handler(error)

@app.errorhandler(IntegrityError)
def handler_integrity_error(error):
    instance.session.rollback()
    return {
         "message":   str(error.orig)
    }, 400

@app.errorhandler(ScanStatusUpdateError)
def handler_scan_completed(error):    
    return common_handler(error)

@app.errorhandler(OperationalError)
def handler_operational(error):
    instance.session.rollback()
    return {
         "message":   str(error.orig)
    }, 400