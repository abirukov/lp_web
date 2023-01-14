from flask import abort, Blueprint, current_app, render_template
from webapp.weather import weather_by_city
from webapp.news.models import News

blueprint = Blueprint('news', __name__)


@blueprint.route("/")
def index():
    title = "Новости Python"
    print(current_app.config["WEATHER_DEFAULT_CITY"])
    weather_param = weather_by_city(current_app.config["WEATHER_DEFAULT_CITY"])
    news_list = News.query.filter(News.text.isnot(None)).order_by(News.published.desc()).all()
    return render_template(
        "news/index.html",
        weather_param=weather_param,
        page_title=title,
        news_list=news_list,
    )


@blueprint.route('/news/<int:news_id>')
def single_news(news_id):
    my_news = News.query.filter(News.id == news_id).first()
    if not my_news:
        abort(404)
    return render_template('news/single_news.html', page_title=my_news.title, news=my_news)
