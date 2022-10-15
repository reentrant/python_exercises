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
contact_key = 0
for contact in contacts:
    contact_key += 1
    sql_command = """
        INSERT INTO person
        VALUES ({}, '{}', '{}');""".format(contact_key, contact.first_name, contact.last_name)
    db.execute(sql_command)

db.execute('CREATE TABLE e_mail_address ' +
          '(key integer, person_key integer, e_mail text)')
e_mails_list = [
    [2, 'fritz@company.com'],
    [1, 'jon@company.com'],
    [1, 'jon@another_mail.com']]
e_mail_key = 0
for person_key, e_mail in e_mails_list:
    e_mail_key += 1
    sql_command = """INSERT INTO e_mail_address VALUES ({}, {}, '{}');
        """.format(e_mail_key, person_key, e_mail)
    db.execute(sql_command)
# Add another e-mail record without contact name
e_mail_key += 1
sql_command = f"INSERT INTO e_mail_address (key, e_mail) VALUES ({e_mail_key}, 'aaron@mail.com');"
db.execute(sql_command)


def execute_sql_statement():
    """
    CROSS JOIN: All rows from both tables. Cartesian Product. DO NOT USE IT!
    English Question: What are all the first names and e-mail addresses I have?
    --SELECT p.first_name,p.last_name
    --FROM person p;
    -- Cartesian product with
    --SELECT e.e_mail
    --FROM e_mail_address e;
    """
    sql_statement = """
    SELECT p.first_name, p.last_name, e.e_mail
    FROM person p JOIN e_mail_address e
    -- ON p.key = e.person_key;
    """
    cursor = db.execute(sql_statement)
    for row in cursor:
        yield row


if __name__ == '__main__':
    for result in execute_sql_statement():
        print(result)
