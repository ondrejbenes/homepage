from . import db


class IpInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(200))
    city = db.Column(db.String(200))
    zip = db.Column(db.String(10))
    lat = db.Column(db.Float())
    lon = db.Column(db.Float())
    timezone = db.Column(db.String(20))
    datetime = db.Column(db.DateTime())
