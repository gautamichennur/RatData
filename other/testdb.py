import mysql.connector
from mysql.connector import errorcode

try:
    # cnn = mysql.connector.connect(
    #     user = 'root',
    #     password = 'root',
    #     database = 'testing',
    #     unix_socket = '/Applications/MAMP/tmp/mysql/mysql.sock'
    # )

    config = {
        'user': 'root',
        'password': 'root',
        'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
        'database': 'testing',
        'raise_on_warnings': True,
    }

    link = mysql.connector.connect(**config)
    print "It works"

except mysql.connector.Error as e:
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print "db access denied"
    elif e.errno == errorcode.ER_BAD_DB_ERROR:
        print "database does not exist"
    else:
        print e

cursor = link.cursor()

addName = "INSERT INTO name (`fname`, `lname`, `id`) VALUES (%s, %s, %s)"
fname = "Wuli"
lname = "Woojin"
id = 3
cursor.execute(addName,(fname,lname,id))
link.commit()
