# redis_connector.py

import redis

class RedisConnector:
    def __init__(self, host, port):
        try:
            self.connection = redis.Redis(host=host, port=port, decode_responses=True)

        except redis.exceptions.ConnectionError as ce:
            print(f"Redis ConnectionError: {ce}")
            raise  
        except redis.exceptions.RedisError as re:
            print(f"Redis Error: {re}")
            raise  

        except Exception as e:
            print(f"An error occurred: {e}")
            raise  
