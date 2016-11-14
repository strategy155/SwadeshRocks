from swadesh_list import app
from flask import flash, request, session, render_template
from models import User, LoginForm
from sqlalchemy.exc import InterfaceError


@app.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        try:
            current_user = User.query.filter(User.name == form.username.data).first()
            if current_user.password == form.password.data:
                session['name'] = current_user.name
                return render_template('login.html', name=current_user.name)
        except InterfaceError:
            flash('Maybe u forgot password, LUL')
    return render_template('login.html', form=form)