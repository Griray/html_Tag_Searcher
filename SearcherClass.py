import time
import requests
import collections
from logger import start_logging
from bs4 import BeautifulSoup as bs


class TagSearcher:

    def __init__(self):
        pass

    def get_check_date(self):
        check_date = time.strftime('%d/%m/%Y')
        return check_date

    def get_html(self, link):
        html_content = requests.get(link)
        return html_content.text

    def get_html_for_test(self, link):
        html_content = requests.get(link)
        return html_content

    def get_html_tags(self, link):
        start_logging().info('Start time of searching tags')
        soup = bs(self.get_html(link), 'html.parser')
        all_tags = []
        for tag in soup.find_all(True):
            all_tags.append(tag.name)
        return all_tags

    def count_tags(self, link):
        start_logging().info(f'{link} web-site is browsing')
        counter = collections.Counter()
        for tag in self.get_html_tags(link):
            counter[tag] += 1
        return dict(counter)
