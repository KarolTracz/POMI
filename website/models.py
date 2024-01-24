from extensions import db


class SignIn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)


class MatchHistory(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.String, unique=True, nullable=False, primary_key=True)
    match_data = db.Column(db.JSON, nullable=False)
