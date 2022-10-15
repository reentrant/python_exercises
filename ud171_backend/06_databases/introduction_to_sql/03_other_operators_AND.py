from collections import namedtuple
import sqlite3

# make a basic Person class
Person = namedtuple('Person', ['first_name', 'last_name', 'e_mail'])
contacts = [ 
    Person('Jon', 'Flanders', 'jon@company.com')]

# make and populate a table
db = sqlite3.connect(':memory:')
db.execute('CREATE TABLE person ' +
          '(first_name text, last_name text, e_mail text)')
db.execute("INSERT INTO person (first_name, last_name) VALUES ('Fritz', 'Onion');")
db.execute("UPDATE person SET e_mail='fritz@company.com' WHERE first_name='Fritz';")

for contact in contacts:
    db.execute('INSERT INTO person VALUES (?, ?, ?);', contact)

db.execute("INSERT INTO person (first_name, last_name) VALUES ('Keith', 'Porteous');")
db.execute("INSERT INTO person (first_name, last_name) VALUES ('Jon', 'McCracken');")
db.execute("INSERT INTO person (first_name, last_name) VALUES ('Jon', 'Ahern');")
db.execute("INSERT INTO person (first_name, last_name) VALUES ('James', 'Lifferth');")
db.execute("INSERT INTO person (first_name, last_name) VALUES ('Brian', 'Curtis');")


def execute_sql_command():
    """
    English question: Who are all the people in my contact list that have the first name Joh and
    their last name is greater than Curtis?
    """
    sql_statement = """
    SELECT p.first_name as FirstName, p.last_name as LastName
    FROM person p
    WHERE p.first_name='Jon' AND p.last_name > 'Curtis'
    -- OR p.birthdate > '12/31/1975'  # -- is a comment in SQL

    """
    cursor = db.execute(sql_statement)

    for row in cursor:
        yield row


if __name__ == '__main__':
    for result in execute_sql_command():
        print(result)
