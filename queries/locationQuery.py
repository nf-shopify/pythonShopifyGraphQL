from client.shopifyClient import shopifyClient
from rich import print


def locationQuery(locationCount, locationEndCursor):
  query = '''
  {
    locations(first: %d  after: %s) {
      nodes {
        id
      }
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
  ''' % (locationCount, locationEndCursor)
  return query


def locationPayload(query):
  # Create the request payload
  payload = {
    'query': query
  }
  return payload


if __name__ == "__main__":
  locationId = None
  locationCount = 1
  locationHasNextPage = True
  locationEndCursor = "null"

  client = shopifyClient()
  locationQ = locationQuery(locationCount, locationEndCursor)
  locationP = locationPayload(locationQ)
  response = client.request("POST", json=locationP)
  print(response.json())
  # print(response.headers)
