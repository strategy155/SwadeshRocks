from flask import request, render_template
from swadesh_list import app
from models import LoginForm, User

@app.route('/')
def index():
    form = LoginForm(request.form)
    if request.method == 'POST':
        User
        return 'LUL'
    return render_template('index_layout.html', form=form)