from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.user.views import get_user_name

article = Blueprint("article", __name__, url_prefix="/article", static_folder="../static")

ARTICLES = {
    1: {
        "title": "Статья 1",
        "text": "Текст статьи 1",
        "author": 2
    },
    2: {
        "title": "Статья 2",
        "text": "Текст статьи 2",
        "author": 2
    },
    3: {
        "title": "Статья 3",
        "text": "Текст статьи 3",
        "author": 1
    },
    4: {
        "title": "Статья 4",
        "text": "Текст статьи 4",
        "author": 3
    }
}


@article.route("/")
def article_list():
    return render_template(
        "articles/list.html",
        articles=ARTICLES
    )


@article.route("/<int:pk>")
def get_article(pk: int):
    if pk in ARTICLES:
        article_raw = ARTICLES[pk]
    else:
        raise NotFound("Article id:{}, not found".format(pk))
    title = article_raw["title"]
    text = article_raw["text"]
    author = get_user_name(article_raw["author"])
    return render_template(
        "articles/details.html",
        title=title,
        text=text,
        author=author
    )
