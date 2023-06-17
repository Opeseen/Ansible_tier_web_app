from . import db;
from flask_login import UserMixin;
from sqlalchemy.sql import func;

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(15),unique=True)
    first_name = db.Column(db.String(15))
    last_name = db.Column(db.String(15))
    password = db.Column(db.Text(150))
    date = db.Column(db.DateTime(timezone=True),default=func.now())

class Record(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    po_number = db.Column(db.String(15))
    invoice_date = db.Column(db.Date)
    due_date = db.Column(db.Date)
    invoice_number = db.Column(db.String(10),unique=True)
    date = db.Column(db.DateTime(timezone=True),default=func.now())
