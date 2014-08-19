import re
import json
from bs4 import BeautifulSoup


class Scrapper(object):
    def __init__(self, html_text):
        self.soup = BeautifulSoup(html_text)
        self.banks = []
        self.regex = re.compile(r'[\n\r\t]')
        self.__get_bank_table()
        self.__get_banks()

    def as_json(self):
        return json.dumps(self.banks)

    def __get_bank_table(self):
        tables = self.soup.find_all('table')
        self.bank_table = tables[3]

    def __get_banks(self):
        rows = self.bank_table.find_all('tr')
        for index in range(2, len(rows)):
            try:
                cols = rows[index].find_all('td')
                bank_uid = self.regex.sub('', cols[0].text).strip()
                bank_name = self.regex.sub('', cols[1].find('a').text).strip()
                self.banks.append({'id': bank_uid, 'name': bank_name})
            except:
                pass
