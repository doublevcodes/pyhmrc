import requests
from typing import Optional

from pyhmrc.oauth import OAuthGenerator

class HelloClient:

    def __init__(self, oauth_token: Optional[str] = None, prod: bool = False) -> None:
        if not oauth_token:
            OAuthGenerator().generate_token('hello')
        self.BASE_URL: str = 'https://api.service.hmrc.gov.uk/hello/' if prod else 'https://test-api.service.hmrc.gov.uk/hello/'
        self.accept_header = {'Accept': 'application/vnd.hmrc.1.0+json'}
        self.endpoints = {
            'world': '/world',
            'user': '/user',
            'application': '/application'
        }

    def hello_world(self):
        request = requests.get(
            f'{self.BASE_URL}{self.endpoints["world"]}',
            headers=self.accept_header
        )
        return request.text

