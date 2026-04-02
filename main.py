import csv
from flask import Flask, redirect, request, render_template

app = Flask(__name__)


class Contact():
    contacts = []
    
    @classmethod
    def search(cls, query):
        return [c for c in cls.contacts if query in c.__repr__()]

    @classmethod
    def all(cls):
        return cls.contacts
        
    def __init__(self, id, first, last, phone, email) -> None:
        self.id = id
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email

    def __repr__(self) -> str:
        return str(self.__dict__)

    def save(self):
        self.contacts.append(self)

with open("test_data.csv", "r", newline="") as test_data:
    reader = csv.reader(test_data)
    for row in reader:
        Contact(*row).save()

@app.route("/")
def index():
    return redirect("/contacts") 

@app.route("/contacts")
def contacts():
    search = request.args.get("q")
    if search:
        contacts_set = Contact.search(search)
    else:
        contacts_set = Contact.all()
    return render_template("index.html", contacts=contacts_set) 

