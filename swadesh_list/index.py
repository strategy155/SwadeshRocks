from flask import request, render_template, session, redirect
from swadesh_list import app
from models import LoginForm, User
from sqlalchemy.exc import InterfaceError


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        print(form.username.data)
        try:
            current_user = User.query.filter(User.name == form.username.data).first()
            if current_user.password == form.password.data:
                session['name'] = current_user.name
                return render_template('index.html', name=current_user.name)
        except InterfaceError:
            redirect('login')
    return render_template('index.html', form=form, name='Guest')