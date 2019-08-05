"""
create a database in MySQL named “python”:

Your MySQL connection id is 9
Server version: 5.6.44-log MySQL Community Server (GPL)

Copyright (c) 2000, 2019, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> CREATE DATABASE python;
Query OK, 1 row affected (0.12 sec)

mysql> connect python
Connection id:    10
Current database: python
mysql> CREATE TABLE vehicles(
    -> id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    -> timestamp VARCHAR(20) NOT NULL,
    -> rpms INT(6) NOT NULL
    -> );
Query OK, 0 rows affected (0.99 sec)

mysql>
"""
import MySQLdb
import mysql.connector
if __name__ == '__main__':
    config = {
        'user': 'jruiz',
        'password': 'Ju,Lian',
        'host': '127.0.0.1',
        'database': 'python',
        'raise_on_warnings': True
    }
    try:
        if False:
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()
            add_rpm = "INSERT INTO vehicles (timestamp, rpms) VALUES (%s, %s)"
            data_rpm = ('2019/07/17,06:48:59', '2000')
            # Insert new register
            cursor.execute(add_rpm, data_rpm)
            cnx.close()
        else:
            # Setup MySQL Connection
            db = MySQLdb.connect(host="localhost", user="jruiz", passwd="Ju,Lian", db="python")
            cursor = db.cursor()
            # Insert a row into our table
            cursor.execute("INSERT INTO vehicles (timestamp, rpms) VALUES ('2019/07/17,19:00:01', 2000)")
            # Save changes to database
            db.commit()
        print("MySQL Commands completed!!!")

    except Exception as e:
        print(e)


