from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

class DataInventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_type = db.Column(db.String(100), nullable=False)
    data_usage = db.Column(db.String(200), nullable=False)
    data_sharing = db.Column(db.String(200), nullable=False)

class ComplianceRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_id = db.Column(db.Integer, db.ForeignKey('data_inventory.id'), nullable=False)
    compliance_type = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    details = db.Column(db.String(500), nullable=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    data_inventory = db.relationship('DataInventory', backref=db.backref('compliance_records', lazy=True))

