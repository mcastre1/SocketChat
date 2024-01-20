import mysql.connector
import hashlib


def hash_password(password):
    # Choosing a secure hashing algorithm, in this case SHA-256
    hash_algorithm = hashlib.sha256()

    # Encoding the password as bytes before hashing
    password_bytes = password.encode('utf-8')

    # Update the hash object with the password bytes
    hash_algorithm.update(password_bytes)

    # Get the hexadecimal representation of the hashed password
    hashed_password = hash_algorithm.hexdigest()

    return hashed_password


# Replace with your database details
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mc255587!",
    database='socketchat'
)

mycursor = db_connection.cursor()

TABLES = {}
TABLES['users'] = """CREATE TABLE `users` (`user_no` int(11) NOT NULL AUTO_INCREMENT,
`name` varchar(255) NOT NULL,
`email` varchar(255) NOT NULL,
PRIMARY KEY (`user_no`))"""
TABLES['accounts'] = """CREATE TABLE `accounts` (`acc_no` int(11) NOT NULL AUTO_INCREMENT,
`account_name` varchar(255) NOT NULL,
`password` varchar(255) NOT NULL,
`user_no` int(11),
PRIMARY KEY (`acc_no`),
FOREIGN KEY (`user_no`) REFERENCES users(`user_no`))"""

# mycursor.execute("CREATE DATABASE socketchat")

# mycursor.execute("SHOW DATABASES")
mycursor.execute("DROP TABLE IF EXISTS accounts")
mycursor.execute("DROP TABLE IF EXISTS users")
# mycursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255))")

for table in TABLES:
    table_query = TABLES[table]
    try:
        print(f"Creating table {table}")
        mycursor.execute(table_query)
    except mysql.connector.Error as err:
        print(err.msg)
    else:
        print("OK")

add_user = ("INSERT INTO users "
            "(name, email)"
            "VALUES (%s, %s)")

user_data = ('Miguel', 'miguelcastrejongal@gmail.com')

mycursor.execute(add_user, user_data)
db_connection.commit()

add_account = ("INSERT INTO accounts "
               "(account_name, password, user_no)"
               "VALUES (%s, %s, %s)")

account_data = ('255589', hash_password('255587'), 1)

mycursor.execute(add_account, account_data)
db_connection.commit()


mycursor.execute("SELECT * FROM users")

for user in mycursor:
    print(user)

# mycursor.execute("SELECT * FROM accounts")

# for account in mycursor:
#    print(account)

mycursor.execute(("SELECT * FROM accounts, users WHERE accounts.password = "
                  "%s"), (hash_password('255587'),))

for row in mycursor:
    print(row)
