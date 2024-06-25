from flask import Flask, jsonify
from config import Base, db_instance
from scan.scan_service import ScanService


app = Flask(__name__)

import routes
import shared.errors.setup

from config import MYSQL_HOST, MYSQL_LIB, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

db_instance.connect(host=MYSQL_HOST, lib=MYSQL_LIB, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DATABASE)

ScanService(instance=db_instance)

Base.metadata.create_all(db_instance.engine)
        