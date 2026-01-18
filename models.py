from ext import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    image = db.Column(db.String(255), default="default_img.png")

# class Comment(db.Model):
#     __tablename__ = "comments"

#     id = db.Column(db.Integer(), primary_key=True)
#     text = db.Column(db.String(), nullable=False)
#     product_id = db.Column(db.Integer(), db.ForeignKey("products.id"))


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    mail = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default="Guest")
    region = db.Column(db.Enum("თბილისი", "ბათუმი", "ქუთაისი", "თელავი", "სხვა...", name="region_enum"))

    def __init__(self, username, mail, password, region, role="Guest"):
        self.username = username
        self.mail = mail
        self.password = generate_password_hash(password)
        self.region = region
        self.role = role



    def check_password(self, password):
        return check_password_hash(self.password, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)