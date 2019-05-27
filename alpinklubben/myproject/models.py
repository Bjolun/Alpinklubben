###################
##### imports #####
###################
#!/usr/bin/env python3

from myproject import db

#######################
##### Model setup #####
#######################

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(15), unique = True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String(20))

    def __init__(self, username, email, password, name):
        self.username = username
        self.email = email
        self.password = password
        self.name = name

class Orders(db.Model):

    __tablename__ = "orders"

    order_id = db.Column(db.Integer, primary_key = True)
    user_ordered = db.Column(db.Integer, db.ForeignKey('users.username'))
    package = db.Column(db.String)
    date = db.Column(db.String)

    def __init__(self, user_ordered, package, date):
        self.user_ordered = user_ordered
        self.package = package
        self.date = date
