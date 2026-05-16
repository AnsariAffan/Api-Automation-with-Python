import requests
from config.config import Config

class BaseClient:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.timeout = Config.TIMEOUT
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json"
        })

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        return self.session.get(url, params=params, timeout=self.timeout)

    def post(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        return self.session.post(url, json=data, timeout=self.timeout)

    def put(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        return self.session.put(url, json=data, timeout=self.timeout)

    def delete(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        return self.session.delete(url, timeout=self.timeout)
