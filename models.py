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
    all_tokens = []
    def render_list(self,words):
        for word in words:
            self.all_tokens.append(StringField(word))
        print(self.all_tokens)
        return self.all_tokens
class LoginForm(Form):
    username = StringField('Username', [validators.DataRequired(), ])
    password = PasswordField('Password', [validators.DataRequired()])
