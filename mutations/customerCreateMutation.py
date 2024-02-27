from rich import print

from client.shopifyClient import shopifyClient


def customerCreateQuery():
  query = '''
  mutation customerCreate($input: CustomerInput!) {
    customerCreate(input: $input) {
    userErrors {
      field
      message
      }
      customer {
      id
      }
    }
  }'''
  return query


def customerCreateInput(email, phone, fname, lname, address1, address2, city, zip):
  input = {
    "email": email,
    "phone": phone,
    "firstName": fname,
    "lastName": lname,
    "acceptsMarketing": True,
    "addresses": [
      {
        "address1": address1,
        "address2": address2,
        "city": city,
        "zip": zip,
        "lastName": lname,
        "firstName": fname,
        "country": "US"
      }
    ]
  }
  return input


def customerCreatePayload(query, input):
  payload = {
    'query': query,
    'variables': {
      'input': input
    }
  }
  return payload


if __name__ == "__main__":
  client = shopifyClient()
  customerCreateQ = customerCreateQuery()
  customerCreateI = customerCreateInput('neilson@test.com', '', 'neilson', 'flemming', '8554 110th', '', 'ricmond hill', '11418')
  customerCreateP = customerCreatePayload(customerCreateQ,customerCreateI)

  #print(customerCreateP)

  response = client.request("POST", json=customerCreateP)
  print(response.json())
  #print(response.headers)
