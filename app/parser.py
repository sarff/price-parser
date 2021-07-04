import requests
import toml
from bs4 import BeautifulSoup
import datetime

config = toml.load("conf/config.toml")
url = config.get('web').get('page')
url_upd = config.get('web').get('page_upd')
replacestr = config.get('web').get('replacestr')

class Parce():
    @staticmethod
    def returntable():
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        quotes = soup.find_all('table', class_='table_price')
        table = ' '.join(map(str, quotes))
        for i in range(len(replacestr)):
            if replacestr[i].find("'") == -1:
                table = table.replace(replacestr[i], "")
            else:
                table = table.replace(replacestr[i], r"\%s" % (replacestr[i]))
        add_date = "<p>Дата прайсу: %s </p>" % datetime.date.today()
        fulltable = "%s %s" % (add_date, table)
        return fulltable



    @staticmethod
    def returntable_upd():
        blacklist = ['a', 'img']
        r = requests.get(url_upd)
        soup = BeautifulSoup(r.text, 'lxml')
        for tag in soup.find_all(True):
            if tag.name in blacklist:
                tag.attrs = {}

        quotes = soup.find_all('table', class_='reliz_tab')
        table = ' '.join(map(str, quotes))
        for i in range(len(replacestr)):
            if replacestr[i].find("'") == -1:
                table = table.replace(replacestr[i], "")
            else:
                table = table.replace(replacestr[i], r"\%s" % (replacestr[i]))
        table = table.replace('border="0"','border="2"')
        add_data = config.get('web').get('add_string_before')
        upd_table = "%s %s" % (add_data, table)

        return upd_table