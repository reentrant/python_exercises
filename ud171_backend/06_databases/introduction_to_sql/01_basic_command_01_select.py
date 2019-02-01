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

for contact in contacts:
    db.execute('INSERT INTO person VALUES (?, ?, ?);', contact)

def basic_sql_command():
    cursor = db.execute("SELECT person.first_name, person.last_name, person.e_mail FROM person;")

    results = []
    for row in cursor:
        person = Person(*row)
        results.append(person)
    return results

if __name__ == '__main__':
    for result in basic_sql_command():
        print result
