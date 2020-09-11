from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class UserOAuth(db.Model, UserMixin):
    id = db.Column(db.String(767), primary_key=True)
    email = db.Column(db.String(767), unique=True, nullable=False)
    name = db.Column(db.Text(), nullable=False)
    profile_pic = db.Column(db.Text(), nullable=False)


    def __init__(self, id_, name, email, profile_pic):
        self.id = id_
        self.name = name
        self.email = email
        self.profile_pic = profile_pic



    @classmethod
    def create(cls, id_, name, email, profile_pic):
        user = cls(id_=id_, name=name, email=email, profile_pic=profile_pic)
        db.session.add(user)
        db.session.commit()
        return user
