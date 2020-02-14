from logger import configure_logging
from news_reader import get_news
from filter import prepare_news
from rendering import render_html_email
from postman import send_email
from feeds import FEEDS


if __name__ == '__main__':
    configure_logging()

    get_news(FEEDS)

    prepare_news(FEEDS)

    send_email(render_html_email(FEEDS))