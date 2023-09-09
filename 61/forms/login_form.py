from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message="Incorrect email format")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, message="Field must be at least 8 "
                                                                                           "characters long")])
    submit = SubmitField("Login")
