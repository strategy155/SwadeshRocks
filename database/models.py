from sqlalchemy import Column, Integer, String
from wtforms import Form, StringField, PasswordField, validators

from database.database_initialization import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    password = Column(String(50))

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password

    def __repr__(self):
        return '<User {}>'.format(self.name)


class RegistrationForm(Form):
    username = StringField('Username')
    password = PasswordField('New Password', [validators.DataRequired(),
                                              validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')