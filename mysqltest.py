import mysql.connector

# Replace with your database details
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mc255587!",
    database='socketchat'
)

mycursor = db_connection.cursor()

TABLES = {}
TABLES['users'] = """CREATE TABLE 'users' ('user_no' int(11) NOT NULL AUTO_INCREMENT,
'name' varchar(255) NOT NULL,
'email' varchar(255) NOT NULL,
PRIMARY KEY ('user_no')"""

# mycursor.execute("CREATE DATABASE socketchat")

# mycursor.execute("SHOW DATABASES")
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
