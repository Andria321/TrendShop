from xml.dom.minidom import Notation
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, RadioField, DateField, SelectField, SubmitField, FileField, EmailField, FloatField 
from wtforms.validators import DataRequired, length, equal_to

from choices import regions


class RegisterForm(FlaskForm):
    username = StringField("შექმენი იუზერნეიმი", validators=[DataRequired()])
    mail = EmailField("შეიყვანე მეილი", validators=[DataRequired()])
    password = PasswordField("შექმენი პაროლი", validators=[DataRequired(), length(min=8, max=32, message="პაროლის სიგრძე უნდა იყოს 8-დან 32 სიმბოლომდე!")])
    confirm_password = PasswordField("გაიმეორე პაროლი", validators=[DataRequired(), equal_to('password', message='პაროლები უნდა ემთხვეოდეს')])
    region = SelectField("შეიყვანე რეგიონი", choices=regions, validators=[DataRequired()])

    submit = SubmitField("რეგისტრაცია")


class LoginForm(FlaskForm):
    username = StringField("შეიყვანე იუზერნეიმი")
    mail = EmailField("შეიყვანე მეილი")
    password = PasswordField("შეიყვანე შენი პაროლი")

    login = SubmitField("შესვლა")


class PaymentForm(FlaskForm):
    full_name = StringField('სახელი, გვარი', validators=[DataRequired(), length(min=2, max=100)])
    card_number = StringField('ბარათის ნომერი',validators=[DataRequired(), length(min=16, max=16)])
    exp_date = DateField('ბარათის ვადა',validators=[DataRequired()])
    cvc = StringField('CVC',validators=[DataRequired(), length(min=3, max=4)])
    location = StringField('თქვენი ლოკაცია', validators=[DataRequired()])

    submit = SubmitField('გადახდა')



class ProductForm(FlaskForm):
    img = FileField("აირჩიე პროდუქტის ფოტო", validators=[DataRequired(), FileAllowed(["jpg", "avif", "webp", "png"])])
    name = StringField("შეიყვანე პროდუქტის სახელი")
    price = FloatField("შეიყვანე პროდუქტის ფასი")

    submit = SubmitField('შექმნა')
        
