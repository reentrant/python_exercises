from collections import namedtuple
import sqlite3

# make a basic Person class
Person = namedtuple('Person', ['first_name', 'last_name'])
contacts = [
    Person('Jon', 'Flanders'),
    Person('Fritz', 'Onion'),
    Person('Keith', 'Porteous'),
    Person('Jon', 'McCracken'),
    Person('Jon', 'Ahern'),
    Person('James', 'Lifferth'),
    Person('Brian', 'Curtis')
    ]

# make and populate a table
db = sqlite3.connect(':memory:')
db.execute('CREATE TABLE person ' +
          '(key integer, first_name text, last_name text)')
i = 0
for contact in contacts:
    i += 1
    populate_sting = """
        INSERT INTO person
        VALUES ({}, '{}', '{}');""".format(i, contact.first_name, contact.last_name)
    db.execute(populate_sting)

db.execute('CREATE TABLE e_mail_address ' +
          '(key integer, person_key integer, e_mail text)')
e_mails_list = [
    [2, 'fritz@company.com'],
    [1, 'jon@company.com'],
    [1, 'jon@another_mail.com']]
i = 0
for person_key, e_mail in e_mails_list:
    i += 1
    populate_sting = """INSERT INTO e_mail_address VALUES ({}, {}, '{}');
        """.format(i, person_key, e_mail)
    db.execute(populate_sting)
i += 1
db.execute("INSERT INTO e_mail_address (key, e_mail) VALUES (" + str(i) + ", 'aaron@mail.com');")

def execute_sql_statement():
    """
    CROSS JOIN: All rows from both tables. Cartesian Product. DO NOT USE IT!
    English Question: What are all the first names and e-mail addresses I have?
    """
    sql_statement = """
    SELECT p.first_name, e.e_mail
    FROM person p JOIN e_mail_address e;
    """
    cursor = db.execute(sql_statement)
    results = []
    for row in cursor:
        results.append(row)
    return results


if __name__ == '__main__':
    for result in execute_sql_statement():
        print result
