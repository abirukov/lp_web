from flask import Blueprint, current_app, render_template
from webapp.weather import weather_by_city
from webapp.news.models import News

blueprint = Blueprint('news', __name__)


@blueprint.route("/")
def index():
    title = "Новости Python"
    weather_param = weather_by_city(current_app.config["WEATHER_DEFAULT_CITY"])
    news_list = News.query.order_by(News.published.desc()).all()
    return render_template(
        "news/index.html",
        weather_param=weather_param,
        page_title=title,
        news_list=news_list,
    )