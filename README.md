# Lana Challenge
Repository for challenge for lana interview

# Overview
This project grants you the possibility to buy merchandising from Lana.
Once all the products are introduced, the total amount will be shown.

For limited time, there are some exclusive offers, so hurry up!
- 3x2 on Pens
- *25% of discount (buying 3 or more T-Shirts)

*Discount will be applied only on T-Shirt, not in the total.

This project had been build with
- Python
- Docker, with a PostgreSQL as DB
- Travis-ci for continuos integration

# How to execute
## Requirements
- Python >= 3.8.5
- Docker >= 20.10.2

## Steps
### 1.- Creating venv: 

Open a terminal on the project's root path ```(./lanaChallenge/)``` and execute

```
python3 -m venv venv
```

### 2.- Install dependencies:

On project's root path, execute:

```
pip3 install -r requirements.txt
```

### 3.- Run Db's container
On project's root path, execute:

```
sudo docker-compose up -d
```

*Option ```-d``` is for detached mode

### 4.- Execute the program

On project's root path, execute:

```
python3 app/main.py
```

### 4.1.- Execute the tests
If you want to run the tests, on project's root path, execute:

```
python3 -m unittest tests.tests
```

# How to run

Once the program is running, you can introduced the products you want separated by commas.

Currently, the only available products are: Pens (PEN), T-Shirts (TSHIRT) and Coffee mugs (MUG).

```
Insert here example photos of console
```
