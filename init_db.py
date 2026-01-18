from ext import db, app
from models import Product, User


with app.app_context():
    db.drop_all()
    db.create_all()
    print("ბაზა წარმატებით შეიქმნა!")
    
    admin = User(
        username="admin", 
        mail="adminmail@gmail.com", 
        password="adminpass", 
        role="Admin",
        region="თბილისი"
    )
    db.session.add(admin)

    moderator = User(
        username="mod", 
        mail="modmail@gmail.com", 
        password="modpass123", 
        role="Moderator",
        region="თბილისი"
    )
    db.session.add(moderator)
    
    db.session.commit()
    print("მომხმარებლები დაემატა!")