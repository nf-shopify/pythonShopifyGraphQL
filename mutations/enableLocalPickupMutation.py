from rich import print

from client.shopifyClient import shopifyClient


def enableLocalPickupQuery():
  query = '''
  mutation enableLocalPickup($localPickupSettings: DeliveryLocationLocalPickupEnableInput!) {
    locationLocalPickupEnable(localPickupSettings: $localPickupSettings) {
      localPickupSettings {
        pickupTime
        instructions
      }
      userErrors {
        message
        field
      }
    }
  }
  '''
  return query


# Create a location payload
def localPickupSettings(locationId):
  localPickupSettings = {
    "locationId": locationId,
    "pickupTime": "TWENTY_FOUR_HOURS",
    "instructions": "Please find an store employee and let them know you are there to pickup"
  }
  return localPickupSettings


# Create the request payload
def enableLocalPickupPayload(query, localPickupSettings):
  payload = {
    'query': query,
    'variables': {
      'localPickupSettings': localPickupSettings
    },
  }
  return payload


if __name__ == "__main__":
  client = shopifyClient()
  enableLocalPickupQ = enableLocalPickupQuery()
  enableLocalPickupD = localPickupSettings('gid://shopify/Location/94237687830')
  enableLocalPickupP = enableLocalPickupPayload(enableLocalPickupQ, enableLocalPickupD)
  response = client.request("POST", json=enableLocalPickupP)
  print(response.json())
  #print(response.headers)
