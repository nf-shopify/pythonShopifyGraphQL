import random

from rich import print

from client.shopifyClient import shopifyClient


def inventorySetQuery():
  query = '''
  mutation inventorySetOnHandQuantities($input: InventorySetOnHandQuantitiesInput!) {
    inventorySetOnHandQuantities(input: $input) {
      userErrors {
        field
        message
      }
      inventoryAdjustmentGroup {
        createdAt
        reason
        referenceDocumentUri
        changes {
          name
          delta
        }
      }
    }
  }
  '''
  return query


def inventorySetInput(inventoryItemId, locationId, quantity):
  input = {
    "reason": "other",
    "setQuantities": [
      {
        "inventoryItemId": inventoryItemId,
        "locationId": locationId,
        "quantity": quantity
      }
    ]
  }
  return input


def inventorySetPayload(query, input):
  payload = {
    'query': query,
    'variables': {
      "input": input
    }
  }
  return payload


if __name__ == "__main__":
  client = shopifyClient()
  inventoryItemId = 'gid://shopify/InventoryItem/49281267302422'
  locationId = 'gid://shopify/Location/94205181974'

  inventorySetQ = inventorySetQuery()
  inventorySetI = inventorySetInput(inventoryItemId, locationId, random.randint(0, 25))
  inventorySetP = inventorySetPayload(inventorySetQ, inventorySetI)

  response = client.request("POST", json=inventorySetP)
  print(response.json())
