from flask import Flask, redirect, request, render_template

app = Flask(__name__)


class Contact():
    def __init__(self) -> None:
        self.id = 1
        self.first = "John"
        self.last = "Smith"
        self.phone = "07555 555555"
        self.email = "john@smith.com"

    def __repr__(self) -> str:
        return str(self.__dict__)
    
    contacts = []

    def save(self):
        self.contacts.append(self)

    @classmethod
    def search(cls, query):
        return [c for c in cls.contacts if query in c.__repr__()]

    @classmethod
    def all(cls):
        return cls.contacts

c_test = Contact()
c_test.save()

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

