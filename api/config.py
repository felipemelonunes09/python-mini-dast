import os

###
### Database configuration
###

from db.MySQLConnection import MySQLConnection
from sqlalchemy.orm import DeclarativeBase

# Database connection env variables
MYSQL_HOST      = os.environ.get('MYSQL_HOST')
MYSQL_LIB       = os.environ.get('MYSQL_HOST_LIB')
MYSQL_PORT      = os.environ.get('MYSQL_PORT')
MYSQL_USER      = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD  = os.environ.get('MYSQL_PASSWORD')
MYSQL_DATABASE  = os.environ.get('MYSQL_DATABASE')

# This variable controls which SQLAlchemy database class is used.
# If another SQLAlchemy library is chosen and a new connection is configured,
# this variable will need to be updated accordingly.
DATABASE_TYPE = os.environ.get('DATABASE')

db_instance = MySQLConnection()

# Define a base class to extends the ORM class with the declarative base.
class Base(DeclarativeBase):
    pass

###
### End Database configuration
###


###
### Websocket configuration
###

WEB_SOCKET_HOST = os.environ.get('WEB_SOCKET_HOST')
WEB_SOCKET_PORT = os.environ.get('WEB_SOCKET_PORT')
