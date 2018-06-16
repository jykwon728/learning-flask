from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField

class SignupForm(Form):
    first_name = StringField('First name', validators = [DataRequired("Please Enter your first name")])
    last_name = StringField('Last name', validators = [DataRequired("Please Enter your last name")])
    email = StringField('Email', validators = [DataRequired("Please Enter your email")])
    password = PasswordField('Password', validators = [DataRequired("Please Enter your password")])
    submit = SubmitField('Sign up')
