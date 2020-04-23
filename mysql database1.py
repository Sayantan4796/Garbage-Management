import mysql.connector
from mysql.connector import errorcode

db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="my_first_db"
  )
db_cursor = db_connection.cursor()
DB_NAME = 'wastebin_attr'

#Creating database table as per requirement'
sql = """CREATE TABLE wastebin_attr (
         Wastebin_serial_number INT,
         Wastebin_type CHAR(20),
         Wastebin_status CHAR(20),
         Wastebin action CHAR(20),
         Wastebin zone CHAR(20),
         Wastebin Lat./Long. CHAR(20) )"""

db_cursor.execute(sql)
 
#Get database table'
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)

#storing the CREATE statements in a Python dictionary called TABLES
cnx = mysql.connector.connect(user='root')
cursor = cnx.cursor()

#make sure the database exists, and create it if not
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

#create the tables by iterating over the items of the TABLES dictionary
for table_name in sql:
    table_description = sql[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        db_cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()

# Insert new data
cnx = mysql.connector.connect(user='root', database='my_first_db')
cursor = cnx.cursor()

add_wastebin_attr = ("INSERT INTO wastebin_attr "
               "(Wastebin_serial_number, Wastebin_type, Wastebin_status, Wastebin action, Wastebin zone, Wastebin Lat./Long.)"
               "VALUES (%d, %s, %s, %s,%s, %s)")

data_wastebin_attr = ('', '', '', '', '', '')

cursor.execute(add_wastebin_attr, data_wastebin_attr)
cnx.commit()

cursor.close()
cnx.close()
