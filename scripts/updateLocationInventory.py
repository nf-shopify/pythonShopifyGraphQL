import random

from rich import print

from client.shopifyClient import shopifyClient
from mutations.activateInventoryMutation import activateInventoryQuery, activateInventoryInput, \
  activateInventoryPayload
from queries.inventoryItemQuery import inventoryItemQuery, inventoryItemPayload
from queries.locationQuery import locationQuery, locationPayload

if __name__ == "__main__":
  # location query parameters
  locationId = None
  locationCount = 1
  locationHasNextPage = True
  locationEndCursor = "null"

  client = shopifyClient()

  while locationHasNextPage == True:
    # query for locations
    locationQ = locationQuery(locationCount, locationEndCursor)
    locationP = locationPayload(locationQ)
    # print(locationQ)

    # make api call to get location data
    response = client.request("POST", json=locationP)
    # print(response.json())
    locationR = response.json()

    # update location query paramaters
    locationId = locationR['data']['locations']['nodes'][0]['id']
    locationHasNextPage = locationR['data']['locations']['pageInfo']['hasNextPage']
    locationEndCursor = '"{}"'.format(locationR['data']['locations']['pageInfo']['endCursor'])
    # print(locationId,locationHasNextPage,locationEndCursor)

    # inventory item query parameters
    inventoryItemId = None
    inventoryItemCount = 1
    inventoryItemHasNextPage = True
    inventoryItemEndCursor = "null"

    while inventoryItemHasNextPage:
      # query for inventory item
      inventoryItemQ = inventoryItemQuery(inventoryItemCount, inventoryItemEndCursor)
      inventoryItemP = inventoryItemPayload(inventoryItemQ)
      # print(inventoryItemQ)

      # make api call to get inventory item data
      response = client.request("POST", json=inventoryItemP)
      # print(response.json())
      inventoryItemR = response.json()

      # update inventory item query paramaters
      inventoryItemId = inventoryItemR['data']['inventoryItems']['edges'][0]['node']['id']
      inventoryItemHasNextPage = inventoryItemR['data']['inventoryItems']['pageInfo']['hasNextPage']
      inventoryItemEndCursor = '"{}"'.format(inventoryItemR['data']['inventoryItems']['pageInfo']['endCursor'])
      # print(inventoryItemId, inventoryItemNextPage, inventoryItemEndCursor)

      # mutation using stored location and inventory
      activateInventoryQ = activateInventoryQuery()
      activateInventoryI = activateInventoryInput(inventoryItemId, locationId, random.randint(0, 25))
      activateInventoryP = activateInventoryPayload(activateInventoryQ, activateInventoryI)

      # make api call to activate and set inventory
      response = client.request("POST", json=activateInventoryP)
      print(f'Status Code: ', response.status_code)

      activateInventoryR = response.json()
      available = activateInventoryR['data']['inventoryActivate']['inventoryLevel']['available']
      apiLimit = activateInventoryR['extensions']['cost']['throttleStatus']['currentlyAvailable']

      # print params
      print(f'Location ID : {locationId})')
      print(f'Item ID : {inventoryItemId}')
      print(f'Available : {available}')
      print(f'API Limit : {apiLimit}')
