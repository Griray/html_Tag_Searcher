import pickle
import sqlite3
from main import start, link, second_level_domain, searcher1

with open('tags_data.pkl', 'wb') as file:
    new_tag_data = pickle.dump(start(), file)


def create_table():
    conn = sqlite3.connect('html_tags.db')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS html_tags(Web_site TEXT, URL TEXT, Check_Date TEXT, Tags BLOB)')

    cur.execute(f"INSERT INTO html_tags VALUES (?, ?, ?, ?)", (second_level_domain, link, searcher1.get_check_date(),
                                                               new_tag_data))
    conn.commit()
    conn.close()


create_table()
