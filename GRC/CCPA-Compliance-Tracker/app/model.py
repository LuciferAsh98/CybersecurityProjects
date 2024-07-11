from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DataInventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_type = db.Column(db.String(100), nullable=False)
    data_usage = db.Column(db.String(200), nullable=False)
    data_sharing = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<DataInventory {self.data_type}>'
