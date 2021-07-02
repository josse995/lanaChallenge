# Lana Challenge
Repository for lana's interview challenge.
Here is the requirements -> [link](https://github.com/josse995/lanaChallenge/blob/dev/Readme.Requirements.md)

# Overview
This project grants the possibility to buy merchandising from Lana.
Once all the products are introduced, the total amount will be shown.

For limited time, there are some exclusive offers, so hurry up!
- 2x1 on Pens
- *25% discount (provided that there is a minimum of 3 t-shirts)

*Discount will be applied only on T-Shirt, not in the total.

This project has been build with
- Python
- Docker, with a PostgreSQL as DB
- Travis-ci for continuos integration (Link to Travis-CI -> [link](https://www.travis-ci.com/github/josse995/lanaChallenge))

# How to execute
## Requirements
This project has been made with:
- Docker >= 20.10.2
- docker-compose >= 1.25.0

## Steps to run

On project's root path, execute:

```
sudo docker-compose up 
```

# Endpoints

## Products
List the products -> ```http://127.0.0.1/api/shop/products```

## Basket
List the basket -> ```http://127.0.0.1/api/shop/basket```
### Create a basket

Method -> POST
Payload -> ```{'products': []}```
Url -> ```http://127.0.0.1/api/shop/basket/```

### Delete a basket
Method -> DELETE
Url -> ```http://127.0.0.1/api/shop/basket/<basket's id>/```

### Add a product to basket
Method -> POST
Payload -> ```{'basket':<basket's id>, 'product':'<PEN | TSHIRT | MUG>'}```
Url -> ```http://127.0.0.1/api/shop/basket/add```

### Get total of a basket
Method -> GET
Url -> ```http://127.0.0.1/api/shop/basket/checkout/?basket=<basket's id>```