from searcher import TagSearcher
from resolve_url import resolve_aliases


link = 'https://' + input('Enter here url without https ')
link = resolve_aliases(link)
searcher1 = TagSearcher(link)
second_level_domain = link[8:link.index('.')]


def start():
    searcher1.get_check_date()
    searcher1.count_tags()
    tags_data = searcher1.count_tags()
    return tags_data


start()
