from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):


    def validate_username(self, username_to_check):
        user =User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exist! Please try a different username')

    def validate_email_addres(self, emailaddress_to_check):
        emailaddress = User.query.filter_by(emailaddress=emailaddress_to_check.data).first()
        if emailaddress:
            raise ValidationError('email already exist! Please try a different email address')

    username = StringField(label='User Name:', validators=[Length(min=2, max=12), DataRequired()])
    emailaddress = StringField(label='Email Address', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')