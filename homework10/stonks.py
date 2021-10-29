import json
from concurrent.futures import ThreadPoolExecutor
from operator import attrgetter
from re import search
from typing import Any, List, Tuple
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
        self.main_site = 'https://markets.businessinsider.com'
        self.stats_to_find = (
            ('latest_price', True),
            ('p_e', False),
            ('year_growth', True),
            ('high_low_diff', True)
        )
        self.filenames_stats = (
            'expensive_price.json',
            'lowest_p_e.json',
            'highest_growth.json',
            'highest_high_low.json'
        )

    def request_contents(self, url: str) -> bytes:
        """
        return contents of page for given url
        """
        response = requests.get(url)
        data = response.content
        return data

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

    def parse_initial_info(self, row) -> None:
        """
        parse html from website to get and store info about company
        """
        url = self.main_site + row[0][0].get('href')
        latest_price = self.strip_digit(row[1].text) * self.exchange_rate
        year_growth = (self.strip_digit(row[-1][2].text[:-1])
                       * self.exchange_rate)
        cmp = Company(url=url, latest_price=latest_price,
                      year_growth=year_growth)
        self.companies.append(cmp)

    def get_companies_from_table(self) -> None:
        """
        get companies and initial data in parallel
        """
        response = self.request_contents(self.snp500_link)
        contents = html.fromstring(response)
        page_rows = contents.xpath('//tr')[1:]
        with ThreadPoolExecutor(max_workers=len(page_rows)) as pool:
            pool.map(self.parse_initial_info, page_rows)

    def parse_company_details(self, company) -> None:
        """
        parse html from company to get and store details about it
        """
        response = self.request_contents(company.url)
        contents = html.fromstring(response)

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

    def get_company_details(self) -> None:
        """
        get details about companies in parallel
        """
        with ThreadPoolExecutor(max_workers=len(self.companies)) as pool:
            pool.map(self.parse_company_details, self.companies)

    def top_10_by_attr(self, args: Tuple[str, bool]) -> List[Company]:
        """
        return sorted list of classes by given attribute
         order descending(default) and ascending
        """
        attribute, reverse = args
        return sorted(self.companies, key=attrgetter(attribute),
                      reverse=reverse)[:10]

    def save_list_to_json(self, args: Tuple[str, List[Any]]) -> None:
        """
        write to file list of classes, json style
        """
        filename, arr = args
        with open(filename, 'w') as file:
            json.dump([cmp.__dict__ for cmp in arr], file, indent=4)

    def save_stats_to_json(self) -> None:
        """
        write top 10 stats to files using threads
        """
        with ThreadPoolExecutor(max_workers=len(self.stats_to_find)) as pool:
            stats = pool.map(self.top_10_by_attr, self.stats_to_find)

        file_and_stats = list(zip(self.filenames_stats, stats))

        with ThreadPoolExecutor(max_workers=len(file_and_stats)) as pool:
            pool.map(self.save_list_to_json, file_and_stats)

    def proccess(self) -> None:
        """
        main execution method
        """
        self.get_exchange_rate()
        self.get_companies_from_table()
        self.get_company_details()
        self.save_stats_to_json()
