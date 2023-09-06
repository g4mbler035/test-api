from fastapi import FastAPI
from database.orm import db_connect as db
from database.orm.Persons import Person

app = FastAPI()


@app.get("/")
def home_page():
    return "Hello Python developers"


@app.get("/persons")
async def get_persons():
    return db.get_persons()
    # person = Person(1, "Aleksa", "stojanovic", "Male", 24)
    # db.add_person(person)


@app.post("/add_person")
async def add_person(id: int, first_name: str, last_name: str, gender: str, age: int):
    person = Person(id, first_name, last_name, gender, age)
    return db.add_person(person)


@app.post("/delete_person")
async def delete_person(first_name: str, last_name: str):
    db.delete_person(first_name, last_name)


@app.post("/update_person")
async def update_person(id: int, first_name: str, last_name: str, gender: str, age: int):
    person = Person(id, first_name, last_name, gender, age)
    db.update_person(id, person)
