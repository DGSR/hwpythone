import json
from operator import attrgetter
from re import search
from typing import Any, List
from xml.etree import ElementTree

import requests
from lxml import html

from constant.html_xml import (CODE_LABEL_QUERY, HIGH_LOW_LABEL_QUERY,
                               NAME_LABEL_QUERY, P_E_LABEL_QUERY, XML_QUERY)


class Company:
    """
    class serves as a data structure
    latest price, company code, p/e, year rise/fall,
     52 week low and 52 week high difference
    """
    def __init__(self, name: str = '', url: str = '',
                 latest_price: float = 0.0, company_code: str = '',
                 p_e: float = 0.0, year_growth: float = 0.0,
                 high_low_diff: float = 0.0):
        self.name = name
        self.url = url
        self.latest_price = latest_price
        self.company_code = company_code
        self.p_e = p_e
        self.year_growth = year_growth
        self.high_low_diff = high_low_diff


class Stonks:
    """
    class that given 2 resource links
     acquires information about companies in s&p 500 to this day such as:
     latest price, company code, p/e, year rise/fall,
     52 week low and 52 week high difference
    """
    def __init__(self):
        self.snp500_link = 'https://markets.businessinsider.com'\
                           '/index/components/s&p_500'
        self.exchange_link = 'http://www.cbr.ru/scripts/XML_daily.asp'
        self.exchange_rate = 0.0
        self.companies = []
        self.expensive_price = []
        self.lowest_p_e = []
        self.highest_growth = []
        self.highest_high_low = []

    def request_contents(self, url: str) -> bytes:
        """
        return contents of page for given url
        """
        return requests.get(url).content

    def strip_digit(self, string: str) -> float:
        """
        return float stripped of any other symbols
        """
        temp = string.replace('\n', '')
        pattern = r'[\d.,]+'
        temp = search(pattern, temp).group()
        return float(temp.replace(',', ''))

    def get_exchange_rate(self) -> None:
        """
        get xml exchange rate from source then parse xml
        updates exchange rate
        """
        res = self.request_contents(self.exchange_link)
        root = ElementTree.fromstring(res)
        self.exchange_rate = float(root.find(XML_QUERY).text.replace(',', '.'))

    def get_companies_from_table(self) -> None:
        """
        parse html from website to get info about companies
         and store them
        """
        contents = html.fromstring(self.request_contents(self.snp500_link))
        page_rows = contents.xpath('//tr')[1:]
        main_site = 'https://markets.businessinsider.com'
        for row in page_rows:
            url = main_site + row[0][0].get('href')
            latest_price = self.strip_digit(row[1].text) * self.exchange_rate
            year_growth = (self.strip_digit(row[-1][2].text[:-1])
                           * self.exchange_rate)
            cmp = Company(url=url, latest_price=latest_price,
                          year_growth=year_growth)
            self.companies.append(cmp)

    def get_company_details(self) -> None:
        """
        parse html from company to get details about companies
         and store them
        """
        for company in self.companies:
            contents = html.fromstring(self.request_contents(company.url))

            name_label = contents.xpath(NAME_LABEL_QUERY)[0].text.strip()
            code_label = contents.xpath(CODE_LABEL_QUERY)[0].text[2:]

            low_label = contents.xpath(HIGH_LOW_LABEL_QUERY)[0][0].text
            low_number = self.strip_digit(low_label)

            high_label = contents.xpath(HIGH_LOW_LABEL_QUERY)[0][1].text
            high_number = self.strip_digit(high_label)

            p_e_label = contents.xpath(P_E_LABEL_QUERY)

            company.name = name_label
            company.company_code = code_label
            company.high_low_diff = (low_number / high_number * 100
                                     * self.exchange_rate)
            if p_e_label:
                company.p_e = (self.strip_digit(p_e_label[0].text)
                               * self.exchange_rate)

    def top_10_by_attr(self, attr: str, reverse: bool = True) -> List[Company]:
        """
        return sorted list of classes by given attribute
         order descending(default) and ascending
        """
        return sorted(self.companies, key=attrgetter(attr),
                      reverse=reverse)[:10]

    def stats_top_10(self) -> None:
        """
        get top 10 stats for companies by different parameters
        """
        self.expensive_price = self.top_10_by_attr('latest_price')
        self.lowest_p_e = self.top_10_by_attr('p_e', False)
        self.highest_growth = self.top_10_by_attr('year_growth')
        self.highest_high_low = self.top_10_by_attr('high_low_diff')

    def save_list_to_json(self, filename: str, arr: List[Any]) -> None:
        """
        write to file list of classes, json style
        """
        with open(filename, 'w') as file:
            json.dump([cmp.__dict__ for cmp in arr], file, indent=4)

    def save_stats_to_json(self) -> None:
        """
        write top 10 stats to files
        """
        self.save_list_to_json('expensive_price.json', self.expensive_price)
        self.save_list_to_json('lowest_p_e.json', self.lowest_p_e)
        self.save_list_to_json('highest_growth.json', self.highest_growth)
        self.save_list_to_json('highest_high_low.json', self.highest_high_low)

    def proccess(self) -> None:
        """
        main execution method
        """
        self.get_exchange_rate()
        self.get_companies_from_table()
        self.get_company_details()
        self.stats_top_10()
        self.save_stats_to_json()
