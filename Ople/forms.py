from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from Ople.models import User


class LoginForm(FlaskForm):

    username = StringField('UserName', validators=[
                           DataRequired()], render_kw={"placeholder": "UserName"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={
                             "placeholder": "Password"})
    submit = SubmitField('LogIn')


class RegistrationForm(FlaskForm):

    email = StringField('Email: ', validators=[
                        DataRequired(), Email()], render_kw={"placeholder": "Email"})
    username = StringField('UserName: ', validators=[DataRequired()], render_kw={
                           "placeholder": "UserName"})
    password = PasswordField('Password: ', validators=[DataRequired(), EqualTo(
        'conf_pass', message="Passwords must match.")], render_kw={"placeholder": "Password"})
    conf_pass = PasswordField('Confirm Password:', validators=[
                              DataRequired()], render_kw={"placeholder": "Confirm password"})
    submit = SubmitField('Register')

    def validate_email(self, email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Email has been already registered.')

    def validate_username(self, username):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError('Username has been already registered.')
