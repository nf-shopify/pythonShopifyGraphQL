from client.shopifyClient import shopifyClient
from rich import print

def Query():
  query = '''
  '''
  return query


def Input():
  input = {}
  return input


def Payload(query, input):
  payload = {
    'query': query,
    "input": input
  }
  return payload

if __name__ == "__main__":
  client = shopifyClient()
  Q = Query()
  I = Input()
  P = Payload()

  response = client.request("POST", json=P)
  print(response.json())
  print(response.headers)
