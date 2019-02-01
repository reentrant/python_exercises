from collections import namedtuple
import sqlite3

# make a basic Person class
Person = namedtuple('Person', ['first_name', 'last_name', 'e_mail'])
contacts = [ 
    Person('Jon', 'Flanders', 'jon@company.com')]

# make and populate a table
db = sqlite3.connect(':memory:')
db.execute('CREATE TABLE contact ' +
          '(first_name text, last_name text, e_mail text)')

for contact in contacts:
    db.execute('INSERT INTO contact VALUES (?, ?, ?);', contact)

def basic_sql_command():
    cursor = db.execute("SELECT first_name, last_name, e_mail FROM contact;")

    results = []
    for row in cursor:
        person = Person(*row)
        results.append(person)
    return results

if __name__ == '__main__':
    print basic_sql_command()