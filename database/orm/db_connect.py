from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

from database.orm.Persons import Person


url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="semperidem@1",
    host="localhost",
    database="quiz"
)


def create_session():
    engine = create_engine(url)

    Person.__table__.create(bind=engine, checkfirst=True)

    Session = sessionmaker(bind=engine)

    return Session()


def add_person(person):
    session = create_session()

    session.add(person)

    session.commit()

def get_persons():
    persons = []

    session = create_session()

    results = session.query(Person).all()

    for result in results:
        person = {f"First name": result.first_name, "Last name": result.last_name, "Gender": result.gender,
                  "Age": result.age}

        persons.append(person)

    session.commit()

    return persons


def delete_person(first_name, last_name):
    session = create_session()

    session.query(Person).filter(Person.first_name == first_name and Person.last_name == last_name).delete()

    session.commit()


def update_person(id, person):
    session = create_session()

    session.query(Person).filter(Person.id == id).update(
        {Person.first_name: person.first_name, Person.last_name: person.last_name, Person.gender: person.gender,
         Person.age: person.age}, synchronize_session=False
    )

    session.commit()

# person = Person(1, "Marko", "Brkusanin", "m", 36)
# person1 = Person(2, "Jelena", "Markovic", "f", 25)
#
# add_person(person1)
