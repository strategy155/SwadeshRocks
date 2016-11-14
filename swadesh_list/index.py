from flask import request, render_template, session, redirect
from swadesh_list import app
from models import LoginForm, User

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm(request.form)
    print(User.query.all())
    if request.method == 'POST' and form.validate():
        current_user = User.query.filter(User.name == form.username).one_or_none()
        if current_user is None:
            redirect('login')
        if current_user.password == form.password:
            session['name'] = current_user.username
        return render_template('index.html', name=current_user.username)
    return render_template('index.html', form=form, name='Guest')