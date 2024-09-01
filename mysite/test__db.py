import pytest
from unittest.mock import patch, MagicMock
import mysql.connector as sql_connector
from mysql.connector import Error


@patch("mysql.connector.connect")
def test_database_creation_success_with_mock(mock_connect):
    mock_db = MagicMock()
    mock_connect.return_value = mock_db
    mock_db.is_connected.return_value = True

    try:
        database = sql_connector.connect(
            host="localhost", user="danargh", passwd="12345"
        )
        assert database.is_connected(), "Failed to connect to MySQL"

        with database.cursor() as cursor_object:
            cursor_object.execute("CREATE DATABASE IF NOT EXISTS db_mvc_django")
            print("Database creation mocked successfully")

    except Error as error:
        pytest.fail(f"Error occurred: {error}")

    finally:
        if database.is_connected():
            database.close()
            print("Mocked database connection closed")


@patch("mysql.connector.connect")
def test_database_creation_failed_with_mock(mock_connect):
    # Simulate failed connection
    mock_connect.side_effect = Error("Failed to connect to MySQL")

    with pytest.raises(Error, match="Failed to connect to MySQL"):
        sql_connector.connect(host="localhost", user="danargh", passwd="12345")
