"""
Connectors.py
"""
from dataclasses import dataclass
from nrobo.selenese import NRobo as nrobo

@dataclass
class ConnectorType:
    """Database Connector Types"""

    MYSQL = "mysql"

@dataclass
class ConnectorAttributes:
    """Database connector attributes"""

    TYPE = "type"
    MAX_RETRY = 5
    MAX_WAIT_BETWEEN_EACH_ATTEMPT = 5


def db_connector(config: {}):
    """Universal Database connector

    Based on CONNECTOR_ATTRIBUTES.TYPE,
    it calls specific db connector.

    For example:

       if config[CONNECTOR_ATTRIBUTES.TYPE] is 'mysql'
          Then it calls mysql_db_connector.

    Possible Connector types are ['mysql']
    """

    # Copy config, remove type attribute from config and pass it to connector
    copy_of_config = config.copy()
    copy_of_config.pop(ConnectorAttributes.TYPE)

    if config[ConnectorAttributes.TYPE] == ConnectorType.MYSQL:
        return mysql_db_connector(config=copy_of_config)
    else:
        raise Exception(
            f"Invalid database connector type: {config[ConnectorAttributes.TYPE]}"
        )


def mysql_db_connector(config: {}):
    """Dedicated database connector to established connection with mysql database instance

    described by given config settings"""

    import mysql.connector
    from mysql.connector import errorcode

    for each_attempt in range(ConnectorAttributes.MAX_RETRY):

        try:
            _db_connection = mysql.connector.connect(**config)
            db_cursor = _db_connection.cursor()

            return {"connection": _db_connection, "cursor": db_cursor}

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

            nrobo.wait(time_in_sec=ConnectorAttributes.MAX_WAIT_BETWEEN_EACH_ATTEMPT)

    raise Exception("Database connection did not established!!!")
