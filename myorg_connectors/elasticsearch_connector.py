# elasticsearch_connector.py

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError, ConnectionTimeout, SSLError

class ElasticsearchConnector:
    def __init__(self, host, port, use_https=False, username=None, password=None, timeout=60):
        # Set the scheme to 'https' if use_https is True
        self.scheme = 'https' if use_https else 'http'
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.timeout = timeout

        try:
            # Set the basic authentication credentials if provided
            if self.username and self.password:
                self.connection = Elasticsearch(
                    [f'{self.scheme}://{self.host}:{self.port}'],
                    http_auth=(self.username, self.password),
                    use_ssl=use_https,
                    verify_certs=False,  # Disable SSL verification
                    timeout=self.timeout
                )
            else:
                self.connection = Elasticsearch(
                    [f'{self.scheme}://{self.host}:{self.port}'],
                    use_ssl=use_https,
                    verify_certs=False,  # Disable SSL verification
                    timeout=self.timeout
                )

        except ConnectionError as ce:
            raise ConnectionError(f"ConnectionError: {ce}")

        except ConnectionTimeout as cte:
            raise ConnectionTimeout(f"ConnectionTimeout: {cte}")

        except SSLError as ssle:
            raise SSLError(f"SSLError: {ssle}")
