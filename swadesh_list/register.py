from flask import request, flash, redirect, render_template, url_for
from sqlalchemy.exc import IntegrityError
from database import db_session
from models import RegistrationForm, User
from swadesh_list import app


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.password.data)
        try:
            db_session.add(user)
            db_session.commit()
            flash('Access granted')
            return redirect(url_for('login'))
        except IntegrityError:
            flash('Username is not unique')
    return render_template('register.html', form=form)