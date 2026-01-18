from email import message
from itertools import product
from flask import Flask, flash, render_template, redirect, session
from forms import PaymentForm, RegisterForm, LoginForm, ProductForm
import os
from ext import app, db
from models import Product, User
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash


            # <-- just in case i need them -->
# products = [
#     {"name": "Stone Island-ის დათბილული ჰუდი", "price": 79, "image": "/static/images/Hoodie.jpg", "id": 0},
#     {"name": "Stone Island-ის ზმეიკიანი ზედა", "price": 49, "image": "/static/images/Zip Jacket.avif", "id": 1},
#     {"name": "Stone Island-ის კანისფერი მოსაცმელი", "price": 109, "image": "/static/images/White Jacket.jpg", "id": 2},
#     {"name": "Stone Island-ის თეთრი მოსაცმელი", "price": 149, "image": "/static/images/White Jacket 2.jpg", "id": 3},
#     {"name": "Stone Island-ის დათბილული ზმეიკიანი ზედა", "price": 89, "image": "/static/images/Zip Kargi.jpg", "id": 4},
#     {"name": "Levis-ს ზედა", "price": 39, "image": "/static/images/Levis.webp", "id": 5},
#     {"name": "Lacoste-ს ზედა", "price": 39, "image": "/static/images/Lacoste.avif", "id": 6},
#     {"name": "Massimo Dutti-ს ჯინსი", "price": 74, "image": "/static/images/Massimo.avif", "id": 7},
# ]


# role = "Guest"
# roli=role --> (details da home)
 
@app.route("/")
def home():
    products = Product.query.all()
    cart_items = len(get_cart_items())
    return render_template("index.html", products=products, cart_items=cart_items)

@app.route("/create_product", methods=["GET", "POST"])
def create_product():
    form = ProductForm()
    if form.validate_on_submit():
        new_product = Product(name=form.name.data, price=form.price.data, )

        image = form.img.data
        img_location = os.path.join(app.root_path, "static", "images", image.filename)
        image.save(img_location)

        new_product.image = image.filename

        db.session.add(new_product)
        db.session.commit()

        flash("პროდუქტი წარმატებით დაემატა", "success")
        return redirect("/")

    return render_template("create_product.html", form=form)


@app.route("/edit_product/<int:product_id>", methods=["POST", "GET"])
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    form = ProductForm(obj=product) 
    
    if form.validate_on_submit():
        if form.img.data:
            file = form.img.data
            filename = file.filename
            file.save(f"static/images/{filename}")        
            product.image = filename 

        product.name = form.name.data
        product.price = form.price.data

        db.session.commit()
        flash("პროდუქტი წარმატებით განახლდა", "success")
        return redirect("/")
    
    return render_template("create_product.html", form=form, product=product)


@app.route("/details/<int:product_id>")
def detailed(product_id):
    product = Product.query.get(product_id)
    # comments = Comment.query.join(Product).filter(Product.id == product_id).all()
    return render_template("Details.html", product=product)

@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(form.username.data == User.username).first()
        if user and user.check_password(form.password.data):
            login_user(user)

            flash("თქვენ წარმატებით გაიარეთ ავტორიზაცია", "success")
            return redirect("/")
        else:
            flash("მოხდა შეცდომა", "danger")


    return render_template("Log In.html", form=form)



@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        existing_mail = User.query.filter_by(mail=form.mail.data).first()

        if existing_user:
            flash("ეს სახელი დაკავებულია მოიფიქრეთ ახალი სახელი.", "danger")
            return redirect("/register")
        
        if existing_mail:
            flash("ეს მეილი უკვე გამოყენებულია.", "danger")
            return redirect("/login")

        new_user = User(
            username=form.username.data,
            mail=form.mail.data,
            password=form.password.data,
            region=form.region.data
        )

        db.session.add(new_user)
        db.session.commit()
        flash("რეგისტრაცია წარმატებით დასრულდა!", "success")
        return redirect("/login")

    return render_template("register.html", form=form)

@app.route("/logout")
def logout():
    logout_user()

    return redirect("/")


@app.route("/delete/<int:product_id>")
def delete(product_id):
    product = Product.query.get(product_id)

    db.session.delete(product)
    db.session.commit()

    flash("პროდუქტი წარმატებით წაიშალა!", "Danger")
    return redirect("/")

@app.route("/contact")
def contact():
    return render_template("Contact.html")

@app.route('/pay', methods=['GET', 'POST'])
def pay():
    form = PaymentForm()
    if form.validate_on_submit():
        return "Payment Successfull"
    return render_template('pay.html', form=form)


def get_cart_items():
    return session.get('cart', []) 


@app.route("/cart")
def cart():
    cart_product_ids = session.get('cart', [])
    length = len(cart_product_ids)
    products = []
    if cart_product_ids:
        products = Product.query.filter(Product.id.in_(cart_product_ids)).all()
    return render_template('cart.html', products=products, cart_items=length)


@app.route("/add_to_cart/<int:item_id>", methods=['GET', 'POST'])
def add_to_cart(item_id):
    cart = session.get('cart', [])
    cart.append(item_id)
    
    session['cart'] = cart
    session.modified = True
    return redirect("/clothing")


@app.route("/remove_from_cart/<int:item_id>")
def remove_from_cart(item_id):
    cart = session.get('cart', [])
    if item_id in cart:
        cart.remove(item_id)
        session['cart'] = cart
        session.modified = True
        
    return redirect("/cart")


@app.route("/clothing")
def tops():
    products = Product.query.all()
    cart_items = len(get_cart_items())
    return render_template("clothing.html", products=products, cart_items=cart_items)