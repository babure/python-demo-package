# mongodb_connector.py

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ConfigurationError, OperationFailure

class MongoDBConnector:
    def __init__(self, host, port, auth_source, database, username, password):
        self.host = host
        self.port = port
        self.auth_source = auth_source
        self.database = database
        self.username = username
        self.password = password

        try:
            self.client = MongoClient(self.host, self.port, username=self.username, password=self.password, authSource=self.auth_source)

        except ConnectionFailure as cf:
            # Handle ConnectionFailure
            raise ConnectionFailure(f"ConnectionFailure: {cf}")

        except ConfigurationError as ce:
            # Handle ConfigurationError
            raise ConfigurationError(f"ConfigurationError: {ce}")

        except OperationFailure as of:
            # Check for authentication failure
            if 'Authentication failed' in str(of):
                raise AuthenticationError(f"AuthenticationError: {of}")
            else:
                # Handle other OperationFailure scenarios
                raise OperationFailure(f"OperationFailure: {of}")

        except Exception as e:
            # Handle all other exceptions
            raise Exception(f"An error occurred: {e}")
