from SearcherClass import TagSearcher
import time

searcher = TagSearcher()
link = 'https://' + input('Enter here url without https ')
second_level_domain = link[8:link.index('.')]


def start():
    searcher.get_check_date()
    time.sleep(0.36)
    searcher.count_tags(link)

    tags_data = searcher.count_tags(link)
    return tags_data

start()