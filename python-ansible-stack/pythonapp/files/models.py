from . import db;
from sqlalchemy.sql import func;

class Record(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    po_number = db.Column(db.String(15))
    invoice_date = db.Column(db.Date)
    due_date = db.Column(db.Date)
    invoice_number = db.Column(db.String(10),unique=True)
    date = db.Column(db.DateTime(timezone=True),default=func.now())
