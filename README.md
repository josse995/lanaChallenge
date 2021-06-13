# Lana Challenge
Repository for lana's interview challenge.

# Overview
This project grants you the possibility to buy merchandising from Lana.
Once all the products are introduced, the total amount will be shown.

For limited time, there are some exclusive offers, so hurry up!
- 2x1 on Pens
- *25% of discount (buying 3 or more T-Shirts)

*Discount will be applied only on T-Shirt, not in the total.

This project has been build with
- Python
- Docker, with a PostgreSQL as DB
- Travis-ci for continuos integration (Link to Travis-CI -> [link](https://www.travis-ci.com/github/josse995/lanaChallenge))

# Structure
This project consists in two docker:
- **lanachallenge_app**, that contains the application in python and communicates with lanachallenge_postgres container
- **lanachallenge_postgres**, that contains the postgres' database 

# How to execute
## Requirements
This project has been made with:
- Docker >= 20.10.2
- docker-compose >= 1.25.0

## Steps

### 1.- Run container
On project's root path, execute:

```
sudo docker-compose up 
```

### 2.- Connect to python app's container
On project's root path, execute:

```
docker exec -it lanachallenge_app /bin/bash
```

### 3.- Execute the program

Execute the following command without changing the path:

```
python3 app/main.py
```

### 4.- Execute the tests
If you want to run the tests, on project's root path, execute:

```
python3 -m unittest tests.tests
```

Or if you don't want to follow all the steps, you can execute directly this command:

```
docker-compose run app sh -c "python3 -m unittest tests.tests"
```

# How to run

Once the program is running, you can introduced the products you want separated by commas.

Currently, the only available products are: Pens (PEN), T-Shirts (TSHIRT) and Coffee mugs (MUG).

<img src="https://github.com/josse995/lanachallenge/blob/dev/resources/example.png">
