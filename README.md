# Program

In order to make sure the program works please make sure all the files are in located in the same directory!

One the program start's running will show a menu and depending on 'option' given you will navigate through all the menu's inside our program.

## Installation

Use the package [PyMySQL](https://pypi.org/project/PyMySQL/) to connect with the mysql db located on remote.

```bash
sudo apt-get install python3-pymysql
```

## Before
Make sure the file contains the following in order to make sure the connection to db and querys work. 

```python
import random
import pymysql
import pymysql.cursors
from dictionaries import *

# In order to stablish connection with the remote db
connection = pymysql.connect(
    host='13.69.10.32',
    user='alumno',
    password='123456789Abc',
    db='db_game',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cur = connection.cursor()

# for example the usage of the stablished connection with the db can be something like this
with cur.cursor() as cursor:
 cursor.execute(
  "INSERT INTO player (player_name, player_risk, player_id, human) VALUES (%s, %s, %s, %s)",
  (new_player_name, new_player_behaviour, new_player_id, 1))
 cur.commit()
 print("Player added successfully!")

# that will INSERT INTO the table 'player' with variables already given
# into the specified columns following the given order


```

## SSH
If you want to access the remote Ubuntu server with SSH then use the following. 

```cmd
# With private key
ssh -i /path/file/proyecto1_key.pem -p [port] alumno@13.69.10.32

# Using credentials
ssh -p [port] alumno@13.69.10.32
```

## Collaborators

Miguel A. Caceres Iriarte - [GitHub](https://github.com/MACIriarte) - [LinkedIn](https://www.linkedin.com/in/miguel-angel-caceres-iriarte-609812182/)

Jordi Abello - [GitHub](https://github.com/jordiabello)

Adrián Romero

## License

[MIT](https://choosealicense.com/licenses/mit/)
