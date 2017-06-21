'''
Database programming using Python

- using `ponyorm`
- ORM i.e Object Relation Mapping is the tool which maps 
  the Python Objects to Database tables and provides sets of 
  object's methods which performs the corresponding database 
  operation (Insert, Update, Delete etc.) for us.
- ORM also supports different relational database engines
- Rather than working with SQLs and its different syntax, 
  we can write the program in Python

installation:

pip install pony

based on what database you need, also required:

PostgreSQL: psycopg or psycopg2cffi package
MySQL: MySQL-python or PyMySQL package
Oracle: cx_Oracle package

'''

from datetime import date
from decimal import Decimal

# STEP1: Import ponyorm
from pony.orm import *

# STEP2: Create the global database object
db = Database()


# STEP3: Bind this database object with the datbase engine (as required)
db.bind('sqlite', ':memory:')
# db.bind('sqlite', 'database.sqlite', create_db=True)

# For PostgreSQL, use:
# db.bind('postgres', user='', password='', host='', database='')

# For MySQL, use:
# db.bind('mysql', host='', user='', passwd='', db='')

# For Oracle, use:
# db.bind('oracle', 'user/password@dsn')

# STEP4: Create the object entities (for each table in db)
class Person(db.Entity):
    name = Required(str, 50)
    age = Required(int)
    email = Optional(str, unique=True)
    salary = Required(Decimal, 10, 2)
    is_student = Required(bool, default=True)
    added_on = Optional(date, default=date.today())
    cars = Set('Car')
    
class Car(db.Entity):
    make = Required(str)
    model = Required(str)
    owner = Required(Person)

    def __str__(self):
        return self.make + " " + self.model

# sql_debug(True)

# STEP5: create the entity to table mappings; 
#        create the tables in db, if not already existed.
#        has to be called after creating entities
db.generate_mapping(create_tables=True)


@db_session
def add_default_records():
    '''adding new records / Insert SQL'''

    '''
    make new objects and call commit(), that's it!

    The db_session() decorator performs the following actions on exiting function:

    - Performs rollback of transaction if the function raises an exception
    - Commits transaction if data was changed and no exceptions occurred
    - Returns the database connection to the connection pool
    - Clears the database session cache
    '''

    p1 = Person(name='abhijit', age=34, email="a@a.com", salary=11.5)
    p2 = Person(name='vishal', age=32, email="a@b.com", salary=12)

    # creating another person with already existing email will raise error:
    # Cannot create Person: value 'a@a.com' for key email already exists
    # p3 = Person(name='mangesh', age=33, email="a@a.com") 
    p3 = Person(name='mangesh', age=33, salary=24) 

    c1 = Car(make='Maruti', model='Ritz', owner=p1)
    c2 = Car(make='Hyundai', model='i10', owner=p2)
    c3 = Car(make='Tata', model='Nano', owner=p2)
    c4 = Car(make='Honda', model='City', owner=p3)

    # not required, will be called by db_session
    # commit()

add_default_records()

with db_session:
      p = Person(name='nitin', age=34, added_on=date(2001,12,15), salary=28)
      Car(make='Audi', model='R8', owner=p) 
      Car(make='Mercedez', model='Benz', owner=p) 
      # commit() will be done automatically
      # database session cache will be cleared automatically
      # database connection will be returned to the pool

with db_session:
    the_person = select(p for p in Person if p.name == 'abhijit').first()
    # print (the_person)

    # updting the record
    # the_person.age -= 1

    # deleting the record
    the_person.delete()

with db_session:
  # fetching records from table - SELECT operation
  persons = select(p for p in Person if p.age >= 33).order_by(Person.name)
  # persons = select(p for p in Person)
  for person in persons:
    print(person.id, person.name, person.age, person.salary, person.email, person.cars, person.added_on.strftime("%d-%m-%y"))


with db_session:
    cars = select(c for c in Car)
    for car in cars:
        print(car.make, car.model, car.owner)





