from client.shopifyClient import shopifyClient
from rich import print

def inventoryItemQuery(inventoryCount, inventoryEndCursor):
  query = '''
  {
    inventoryItems(first: %d  after: %s) {
      edges {
        node {
          id
        }
      }
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }''' % (inventoryCount, inventoryEndCursor)
  return query

def inventoryItemPayload(query):
  # Create the request payload
  payload = {
    'query': query
  }
  return payload


if __name__ == "__main__":
  inventoryItemId = None
  inventoryCount = 1
  inventoryHasNextPage = True
  inventoryEndCursor = "null"

  client = shopifyClient()
  inventoryItemQ = inventoryItemQuery(inventoryCount,inventoryEndCursor)
  inventoryItemP = inventoryItemPayload(inventoryItemQ)
  response = client.request("POST", json=inventoryItemP)
  #print(response.json())
  r = response.json()
  inventoryItemId = r['data']['inventoryItems']['edges'][0]['node']['id']
  inventoryItemNextPage = r['data']['inventoryItems']['pageInfo']['hasNextPage']
  inventoryItemEndCursor = '"{}"'.format(r['data']['inventoryItems']['pageInfo']['endCursor'])
  print(inventoryItemId, inventoryItemNextPage, inventoryItemEndCursor)
  # print(response.headers)
