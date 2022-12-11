from flask import Flask

from webapp.model import db, News
from webapp.python_org_news import get_python_news
from webapp.weather import weather_by_city
from flask import render_template


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)

    @app.route("/")
    def index():
        title = "Новости Python"
        weather_param = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
        news_list = News.query.order_by(News.published.desc()).all()
        return render_template(
            "index.html",
            weather_param=weather_param,
            page_title=title,
            news_list=news_list,
        )

    return app
