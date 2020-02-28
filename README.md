# Homework
Simple dockerized Flask web app with Python and MySQL. \
Commands below prepared for localhost:5000.

## Building and running  

Run `run.sh` to build the app and run it on port 5000 by default. You can choose port by passing argument.\
Command to run application with changed port on 4567 `./run.sh 4567`.\
Bring it down with `docker-compose down`.\
Commands are prepared without sudo. \
Managing Docker as a non-root user: [https://docs.docker.com/install/linux/linux-postinstall/](https://docs.docker.com/install/linux/linux-postinstall/)

## Database
MySQL database main is initialized with two coulmn table employees by init.sql.
Colums 'id' and 'name'.

Example with data inside:
|id |   name |
|:-:|:------:|
| 1 | Adam   | 
| 2 | Bridget|
| 3 | Charlie|

Files docker-compose.yml and main.py contain visible credentials!
#### Checking database
* Go to db container by typing `docker exec -it homework-master_db_1 /bin/bash` 
* `mysql -u root -p` and then password `test`(default)
* `SHOW DATABASES;` to list databases. We look for main
* `USE main;`
* `DESCRIBE employees;` or `SELECT * FROM employees;`
 
## Testing

### Tools
* cURL [https://curl.haxx.se/](https://curl.haxx.se/) 
* Postman [https://www.postman.com/](https://www.postman.com/)

### host:port/echo
This endpoint expects json payload, return data and insert to database.
DB table has two columns: id, name.

#### cURL
* Type```curl -X POST -H 'Content-Type: application/json' http://localhost:5000/echo -d '{"id": "1", "name": "Adam"}'```
* Returned data in terminal. Check database for inserted id and name. 
#### Postman
* Choose POST option and http://localhost:5000/echo address
* In BODY section set RAW option and JSON(application/json) format
* Add data to textbox {"id": "1", "name": "Adam"} and click SEND 
* Returned data in response window. Check database for inserted id and name.

### host:port/random
Endpoint returns random number from 0 to 100.
#### cURL
* Type `curl localhost:5000/random`

#### Postman
* Choose GET option and http://localhost:5000/random
* Click SEND 

### host:port/list
Endpoint returns data from database.

#### cURL
* Type `curl localhost:5000/list`

#### Postman
* Choose GET option and http://localhost:5000/list
* Click SEND 
