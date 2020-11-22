from searcher import TagSearcher
import time

link = 'https://' + input('Enter here url without https ')
searcher1 = TagSearcher(link)
second_level_domain = link[8:link.index('.')]


def start():
    searcher1.get_check_date()
    time.sleep(0.36)
    searcher1.count_tags()
    tags_data = searcher1.count_tags()
    return tags_data


start()
