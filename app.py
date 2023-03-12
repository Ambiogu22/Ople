from flask import render_template, redirect, url_for
from flask_login import login_required, login_user, logout_user
from Ople import app, db
from Ople.forms import RegistrationForm, LoginForm
from Ople.models import User

# OPLE PROJECT STARTED 03/09/2023


@app.route('/', methods=["GET", "POST"])
def index():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()

        if user.checkPassword(form.password.data) and user is not None:

            login_user(user)

            return redirect(url_for('main'))
        else:
            return redirect(url_for('index'))

    return render_template('index.html', form=form)


@app.route('/register', methods=["GET", "POST"])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():

        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('registration.html', form=form)


@app.route('/main')
@login_required
def main():
    return render_template('main.html')


@app.route('/my_posts')
@login_required
def my_posts():
    return render_template('my_posts.html')


@app.route('/setting')
@login_required
def settings():
    return render_template('settings.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
