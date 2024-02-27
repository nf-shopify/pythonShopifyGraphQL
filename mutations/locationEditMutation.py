from random_address import real_random_address
from rich import print

from client.shopifyClient import shopifyClient


def locationEditQuery():
  query = '''
  mutation locationEdit($id: ID!, $input: LocationEditInput!) {
  locationEdit(id: $id, input: $input) {
    location {
      id
      name
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
def locationEditInput(locationId, address1, address2, city, zip):
  input = {
    "id": locationId,
    "input": {
      "address": {
        "address1": address1,
        "address2": address2,
        "city": city,
        "countryCode": "US",
        "zip": zip
      },
      "fulfillsOnlineOrders": True
    }
  }
  return input


# Create the request payload
def locationEditPayload(query, Input):
  payload = {
    'query': query,
    'variables': Input
  }
  return payload


if __name__ == "__main__":
  client = shopifyClient()
  locationEditQ = locationEditQuery()
  address = real_random_address()
  locationEditI = locationEditInput('gid://shopify/Location/94237392918', address["address1"], address["address2"],
                                address["city"], address["postalCode"])
  print(locationEditI)
  locationEditP = locationEditPayload(locationEditQ, locationEditI)
  print(locationEditP)
  response = client.request("POST", json=locationEditP)
  print(response.json())
  r = response.json();
  #print(response.headers)
