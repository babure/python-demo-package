# mongodb_connector.py

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ConfigurationError, OperationFailure

class MongoDBConnector:
    def __init__(self, host, port, auth_source, database, username, password):
        try:
            self.client = MongoClient(host, port, username=username, password=password, authSource=auth_source)
            self.db = self.client[database]
        except ConnectionFailure as cf:
            raise ConnectionFailure(f"ConnectionFailure: {cf}")
        except ConfigurationError as ce:
            raise ConfigurationError(f"ConfigurationError: {ce}")
        except OperationFailure as of:
            if 'Authentication failed' in str(of):
                raise AuthenticationError(f"AuthenticationError: {of}")
            else:
                raise OperationFailure(f"OperationFailure: {of}")
        except Exception as e:
            raise Exception(f"An error occurred: {e}")
