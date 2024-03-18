from rich import print

from random_address import real_random_address

from queries.locationQuery import locationQuery, locationPayload
from mutations.locationEditMutation import locationEditQuery, locationEditInput, locationEditPayload
from client.shopifyClient import shopifyClient

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
    #print(response.json())
    locationR = response.json()

    # update location query paramaters
    locationId = locationR['data']['locations']['nodes'][0]['id']
    locationHasNextPage = locationR['data']['locations']['pageInfo']['hasNextPage']
    locationEndCursor = '"{}"'.format(locationR['data']['locations']['pageInfo']['endCursor'])
    # print(locationId,locationHasNextPage,locationEndCursor)

    # generate real random address
    address = real_random_address()
    while not address.get('city'):
      address = real_random_address()
    print(address)

    # create lcation update payloado
    locationEditQ = locationEditQuery()
    locationI = locationEditInput(locationId, address['address1'], address['address2'],
                              address['city'], address['postalCode'])

    locationEditP = locationEditPayload(locationEditQ, locationI)
    response = client.request("POST", json=locationEditP)
    print(response.json())

    # print params
    print(f'Update Params : {locationI})')



