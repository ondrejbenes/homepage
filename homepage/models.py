from . import db


class IpInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(80), unique=True, nullable=False)
