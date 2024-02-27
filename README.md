# Python Shopify GraphQL Library

This library contains Shopify GraphQL quieries and mutations targeting the Admin API. 

## Create .env file

```bash
touch .env
```

## Set enviorment variables in .env file

```python
# shopify test instance
STORE="test" #test.myshopify.com
TOKEN="97658a0cdb96e893189y8391hub23"
ACCESSTOKEN = "shpat_5f970b05ae1982381u23h3215464d"
```

## Usage

```python
from client.shopifyClient import client

# create new instance of the client
client = shopifyClient()

# use client in making API calls
client.request("POST", json='')
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
