import os

import requests
from dotenv import load_dotenv
from rich import print

load_dotenv()


class shopifyClient(requests.Session):
  def __init__(self) -> None:
    super().__init__()
    self.store = os.getenv('STORE')
    self.token = os.getenv('TOKEN')
    self.accessToken = os.getenv('ACCESSTOKEN')
    self.baseUrl = f"https://{self.store}.myshopify.com/admin/api/2021-07/graphql.json"
    self.headers.update(
      {"X-Shopify-Access-Token": self.accessToken}
    )

  def request(self, method, *args, **kwargs):
    return super().request(method, self.baseUrl, *args, **kwargs)


if __name__ == "__main__":
  client = shopifyClient()

  response = client.request("POST", json='')
  print(response.json())
  print(response.headers)
