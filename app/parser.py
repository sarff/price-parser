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
        add_data = r'<h6><span style="font-size: 14pt;">Доверьте профессионалам обновление Вашей 1С</span><img style="margin: 5px 0px 10px; float: right;" src="images/update1c.png" alt="update1c" width="400" height="229" /></h6><div><p style="line-height: 24px;">&nbsp;</p><ul style="margin-top: 0px; margin-bottom: 10px;"><li style="line-height: 24px;"><span style="font-size: 12pt;">Своевременное обновление</span></li><li style="line-height: 24px;"><span style="font-size: 12pt;">Профилактические работы</span></li><li style="line-height: 24px;"><span style="font-size: 12pt;">Резервное копирование</span></li><li style="line-height: 24px;"><span style="font-size: 12pt;">Сохранение прошлых доработок</span></li></ul></div><div>'
        upd_table = "%s %s" % (add_data, table)

        return upd_table