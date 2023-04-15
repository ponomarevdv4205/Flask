from flask import Flask

from blog.article.views import article
from blog.user.views import user
from blog.index.views import index
from blog.report.views import report

VIEWS = [
    index,
    user,
    article,
    report
]


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    for view in VIEWS:
        app.register_blueprint(view)
