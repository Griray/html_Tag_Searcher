import collections
import logging
import time
import requests
from bs4 import BeautifulSoup as bs


class TagSearcher:

    def __init__(self, link: str):
        self.link = link

    @staticmethod
    def get_check_date():
        check_date = time.strftime('%d/%m/%Y')
        return check_date

    def get_html(self):
        html_content = requests.get(self.link)
        if html_content.ok:
            return html_content.text
        else:
            return 'Bad Response!'

    def get_html_tags(self):
        logging.info('Start time of searching tags')
        soup = bs(self.get_html(), 'html.parser')
        all_tags = []
        for tag in soup.find_all(True):
            all_tags.append(tag.name)
        return all_tags

    def count_tags(self):
        logging.info(f'{self.link} web-site is browsing')
        counter = collections.Counter()
        for tag in self.get_html_tags():
            counter[tag] += 1
        return dict(counter)
