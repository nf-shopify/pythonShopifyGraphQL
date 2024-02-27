import random

from rich import print

from client.shopifyClient import shopifyClient

def activateInventoryQuery():
  query = '''
    mutation ActivateInventoryItem($inventoryItemId: ID!, $locationId: ID!, $available: Int) {
      inventoryActivate(inventoryItemId: $inventoryItemId, locationId: $locationId, available: $available) {
        inventoryLevel {
          id
          available
          item {
            id
          }
          location {
            id
          }
        }
      }
    }'''
  return query


def activateInventoryInput(inventoryItemId, locationId, available):
  input = {
    "inventoryItemId": inventoryItemId,
    "locationId": locationId,
    "available": available
  }
  return input


def activateInventoryPayload(query, input):
  payload = {
    'query': query,
    'variables': input,
  }
  return payload


if __name__ == "__main__":
  client = shopifyClient()
  inventoryItemId = 'gid://shopify/InventoryItem/49281267302422'
  locationId = 'gid://shopify/Location/94205181974'

  activateInventoryQ = activateInventoryQuery()
  activateInventoryI = activateInventoryInput(inventoryItemId, locationId, random.randint(0, 25))
  activateInventoryP = activateInventoryPayload(activateInventoryQ, activateInventoryI)


  response = client.request("POST", json=activateInventoryP)
  print(response.json())


