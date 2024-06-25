from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class MySQLConnection():
    """
    A class to manage a connection to a MySQL database using SQLAlchemy.

    Attributes:
        - engine: SQLAlchemy engine object for the database connection.
        - Session: SQLAlchemy sessionmaker object for creating sessions.
        - session: SQLAlchemy session object for the active connection.
        - connected: Boolean indicating whether the connection is active.

    Methods:
        - connect(host, lib, port, user, password, database): Establishes a connection to the database.
        - disconnect(): Closes the connection to the database.
    """
    def __init__(self,):
        self.engine = None
        self.Session = None
        self.session = None
        self.connected = False

    def connect(self, host: str, lib: str, port: str, user: str, password: str, database: str):
        """
        Establishes a connection to the MySQL database.

        Args:
            - host: The hostname or IP address of the database server.
            - lib: The SQLAlchemy library to use for the connection (e.g., 'pymysql', 'mysqlconnector').
            - port: The port number to connect to on the database server.
            - user: The username for the database connection.
            - password: The password for the database connection.
            - database: The name of the database to connect to.

        """
        connection_str = f'mysql+{lib}://{user}:{password}@{host}:{port}/{database}'

        self.engine = create_engine(connection_str)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        self.connected = True
        print("Connected to MySQL database")

    def disconnect(self):
        """
        Closes the connection to the MySQL database.
        """
        if self.session:
            self.session.close()
        if self.engine:
            self.engine.dispose()

        self.connected = False
        print("Disconnected from MySQL database")

    def get_session(self):
        """Returns the current session."""
        return self.session
    
    def get_engine(self):
        """Returns the current database engine."""
        return self.engine

