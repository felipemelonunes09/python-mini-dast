import unittest
from unittest.mock import patch, MagicMock

from sqlalchemy.orm import sessionmaker

from db.MySQLConnection import MySQLConnection

class MySQLConnectionTest(unittest.TestCase):

    @patch('sqlalchemy.create_engine')
    def test_connect_success(self, mock_create_engine):
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine

        from config import MYSQL_HOST, MYSQL_LIB, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

        connection = MySQLConnection()
        connection.connect(host=MYSQL_HOST, lib=MYSQL_LIB, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DATABASE)

        self.assertTrue(connection.connected)
        self.assertIsInstance(connection.Session, sessionmaker)  


    @patch('sqlalchemy.create_engine')
    def test_connect_failure(self, mock_create_engine):
        mock_create_engine.side_effect = Exception('Connection failed')

        connection = MySQLConnection()

        with self.assertRaises(Exception):
            connection.connect()

        self.assertFalse(connection.connected)
        self.assertIsNone(connection.engine)
        self.assertIsNone(connection.Session)
        self.assertIsNone(connection.session)
