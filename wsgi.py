from blog.app import db, app
from blog.models import User, Tag, Article
import os

# @app.cli.command("init-db")
# def init_db():
#     """
#     Run in your terminal:
#     flask init-db
#     """
#     db.create_all()
#     print("done!")

@app.cli.command("create-users")
def create_users():
    james = User(first_name="Lora", last_name="Surname" ,username="lora", email='lana@mail.ru')
    nina = User(first_name="Helen", last_name="Surname" ,username="helen", email='helen@mail.ru')
    db.session.add(nina)
    db.session.add(james)
    db.session.commit()
    print("done! created users:", nina)

@app.cli.command("create-admin")
def create_admin():
    admin = User(first_name="Admin", last_name="Surname",username="admin2", is_staff=True, email='admin@mail.ru', password=os.environ.get("ADMIN_PASSWORD"))
    db.session.add(admin)
    db.session.commit()
    print("done! created users:", admin)

@app.cli.command("add-password")
def add_password():
    user=User.query.filter_by(username="admin2").one_or_none()
    user.password=os.environ.get("ADMIN_PASSWORD")
    db.session.commit()
    print("add password:", user)

@app.cli.command("delete-user")
def delete_user():
    users=User.query.delete()
    db.session.commit()
    print("delete:", users)

@app.cli.command("create-tags")
def create_tags():
    for name in ['flask','django','python','sqlalchemy','news',]:
        tag=Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print("done! created tags")

@app.cli.command("delete-article")
def delete_article():
    article=Article.query.filter_by(id=3).delete()
    db.session.commit()
    print("delete:", article)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True
    )