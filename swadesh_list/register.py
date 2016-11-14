from flask import request, flash, redirect, render_template, url_for
from swadesh_list import app
from database.database_initialization import db_session
from database.models import RegistrationForm, User


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.password.data)
        db_session.add(user)
        flash('Access granted')
        return redirect(url_for('login'))
    return render_template('register.html',form=form)