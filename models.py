from sqlalchemy import Column, Integer, String, Enum
from wtforms import Form, StringField, PasswordField, validators, FieldList
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    password = Column(String(50))
    swadesh = Enum()

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password

    def __repr__(self):
        return '<User {}>'.format(self.name)

    def commit_swad(self, enum):
        self.swadesh = enum



class RegistrationForm(Form):
    username = StringField('Username')
    password = PasswordField('New Password', [validators.DataRequired(),
                                                validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')


class SwadeshForm(Form):       
    def render_list(self,words):
        all_tokens = FieldList(StringField())
        for word in words:
            all_tokens.append_entry()

class LoginForm(Form):
    username = StringField('Username', [validators.DataRequired(), ])
    password = PasswordField('Password', [validators.DataRequired()])
