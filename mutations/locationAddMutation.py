from client.shopifyClient import shopifyClient
from random_address import real_random_address
from rich import print

def locationAddQuery():
  query = '''
  mutation locationAdd($location: LocationAddInput!) {
    locationAdd(input: $location) {
      location {
        id
      }
      userErrors {
        field
        message
      }
    }
  }
  '''
  return query

# Create a location payload
def locationAddInput(name, address1, address2, city, zip):
  input = {
    "address": {
      "address1": address1,
        "address2": address2,
        "city": city,
        "countryCode": "US",
        "zip": zip
    },
    "fulfillsOnlineOrders": True,
    "name": name
  }
  return input

#Create the request payload
def locationAddPayload(query,input):
  payload = {
    'query': query,
    'variables': {
      'location': input
    },
  }
  return payload

if __name__ == "__main__":
  client = shopifyClient()
  locationAddQ = locationAddQuery()
  address = real_random_address()
  locationI = locationAddInput('Test Store', address["address1"], address["address2"],
                            address["city"], address["postalCode"])
  locationAddP = locationAddPayload(locationAddQ,locationI)
  response = client.request("POST", json=locationAddP)
  print(response.json())
  print(response.headers)
