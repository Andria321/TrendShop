👔 Trend Shop
Trend Shop is a modern e-commerce platform built for the style-conscious man. This application showcases the latest in trending menswear, offering a streamlined shopping experience from browsing to checkout.

🚀 Key Features
Curated Collection: A focus on current, high-trend men's fashion and apparel.

Secure Checkout: Integrated Flask-WTF for validated and secure customer information forms.

Relational Database: Powered by Flask-SQLAlchemy to manage inventory, categories, and user data.

Clean UI: A minimalist design aesthetic to match modern fashion trends.

🛠️ The Tech Stack
Framework: Flask

Database: SQLAlchemy (Relational Mapping)

Form Handling: WTForms

Environment: Python venv

⚙️ Quick Start Guide
1. Clone & Enter
Bash

git clone https://github.com/yourusername/trend-shop.git
cd trend-shop
2. Prepare Environment
Bash

# Create venv
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
3. Install Requirements
Bash

pip install Flask Flask-SQLAlchemy Flask-WTF
4. Database Initialization
In your terminal, run the following to set up your product tables:

Bash

python
>>> from app import db
>>> db.create_all()
>>> exit()
5. Launch
Bash

flask run
Local link: http://127.0.0.1:5000/

📁 Architecture
app.py — The heart of the application and route handling.

models.py — Defines the data structure for clothing items and orders.

forms.py — Custom classes for login, registration, and shipping forms.

templates/ — Jinja2 HTML templates for a dynamic frontend.

static/ — CSS styles and high-resolution product imagery.



============================================================================
============================================================================
============================================================================



👔 Trend Shop - მამაკაცის ტრენდული სამოსის მაღაზია
Trend Shop არის თანამედროვე ელექტრონული კომერციის პლატფორმა, რომელიც შექმნილია სპეციალურად მოდური მამაკაცებისთვის. აპლიკაცია საშუალებას აძლევს მომხმარებელს დაათვალიეროს უახლესი კოლექციები, გამოიყენოს ფილტრები და მარტივად განათავსოს შეკვეთა.

🚀 ძირითადი ფუნქციები
კურატული კოლექცია: აქცენტი თანამედროვე და მოდურ მამაკაცის ტანსაცმელზე.

უსაფრთხო ფორმები: მომხმარებლის მონაცემების ვალიდაცია და დაცვა Flask-WTF-ის გამოყენებით.

მონაცემთა ბაზა: ინვენტარის, კატეგორიებისა და მომხმარებლების მართვა Flask-SQLAlchemy-ის მეშვეობით.

მინიმალისტური დიზაინი: სუფთა და სწრაფი ინტერფეისი საუკეთესო სამომხმარებლო გამოცდილებისთვის.

🛠️ ტექნოლოგიური სტეკი
Backend: Flask (Python-ის ფრეიმვორკი)

ORM (ბაზა): SQLAlchemy

ფორმების მართვა: WTForms

გარემო: Python venv (ვირტუალური გარემო)

⚙️ ინსტალაცია და კონფიგურაცია
მიჰყევით ამ ნაბიჯებს პროექტის ლოკალურად გასაშვებად:

1. რეპოზიტორის კლონირება
Bash

git clone https://github.com/yourusername/trend-shop.git
cd trend-shop
2. ვირტუალური გარემოს შექმნა
Bash

# გარემოს შექმნა
python -m venv venv

# გააქტიურება (Windows)
venv\Scripts\activate

# გააქტიურება (Mac/Linux)
source venv/bin/activate
3. საჭირო ბიბლიოთეკების ინსტალაცია
Bash

pip install Flask Flask-SQLAlchemy Flask-WTF
4. მონაცემთა ბაზის ინიციალიზაცია
ტერმინალში ჩაწერეთ შემდეგი ბრძანებები ბაზის ცხრილების შესაქმნელად:

Bash

python
>>> from app import db
>>> db.create_all()
>>> exit()
5. აპლიკაციის გაშვება
Bash

flask run
საიტი ხელმისაწვდომი იქნება მისამართზე: http://127.0.0.1:5000/

📁 პროექტის სტრუქტურა
app.py — აპლიკაციის მთავარი ფაილი და როუტინგი.

models.py — მონაცემთა ბაზის მოდელები (ტანსაცმელი, ზომები, ფასები).

forms.py — რეგისტრაციის, ავტორიზაციისა და შეკვეთის ფორმები.

templates/ — Jinja2 HTML შაბლონები.

static/ — CSS სტილები და პროდუქციის ფოტოები.
