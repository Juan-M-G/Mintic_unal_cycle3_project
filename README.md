# Mintic_unal_cycle3_project

This is a project made for MisionTic2022 program whit the National University. It's about sales system for a shop (In this case a Icecream Shop), compose by the BackEnd developed on Django Rest Framework and connected to a PostgreSQL database.🧷

## Model

| **Users** |
|------------- |
| Id |
|Username|
|Password|
|Name|
|Email|

|**Bills**|
|------------- |
|Id_bill|
|date|
|client_name|
|user_id `(Fk)`|
|isActive|

|**Products**|
|------------- |
|Id_prod|
|Name|
|Product_amount|
|Unity_cost|
|isActive|

### Midd Table

|**Bill_product**|
|------------- |
|Id|
|Bill_id `(Fk)`|
|Product_id `(Fk)`|
|Amount|
|Subtotal|

# Features

1.  Usage of Auth Token.
2. Create, update, and consult new users and products.
3. Create new bills.
4. Generate a general report of sales.
