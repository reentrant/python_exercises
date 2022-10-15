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


def execute_sql_statement():
    """
    English question: Who are all the people in my contact list ordered by last name?
    """
    sql_statement = """
    SELECT p.last_name, p.first_name
    FROM person p
    ORDER BY p.last_name ASC;
    """
    cursor = db.execute(sql_statement)

    for row in cursor:
        yield row


if __name__ == '__main__':
    for result in execute_sql_statement():
        print(result)
