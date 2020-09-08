from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import PasswordType
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(
        PasswordType(schemes=['pbkdf2_sha512']),
        unique=False,
        nullable=True,
    )
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

    @classmethod
    def add(cls, email, password):
        user = cls(email=email, password=password, is_active=True)
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def get(cls, user_id):
        return cls.query.filter_by(id=user_id).one_or_none()

    @classmethod 
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).one_or_none()


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