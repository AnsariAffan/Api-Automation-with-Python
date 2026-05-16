import requests
from config.config import Config

class BaseClient:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.timeout = Config.TIMEOUT
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://fakestoreapi.com/"
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
