from unittest.mock import MagicMock, Mock, patch

import lxml  # noqa: F401

from homework10.stonks import Stonks


def test_stonks_strip_digit():
    assert Stonks.strip_digit(Stonks, '\\r\\n2,048') == 2048.0
    assert Stonks.strip_digit(Stonks, 'Hello0.451Darkness') == 0.451


def test_stonks_exchange_rate():
    tmp = Stonks()
    xml = '<Something><Valute ID="R01235">'\
          '<Value>30,05</Value>'\
          '</Valute></Something>'
    with patch('homework10.stonks.Stonks.request_contents', return_value=xml):
        tmp.get_exchange_rate()
        assert tmp.exchange_rate == 30.05


def test_parse_initial_info():
    tmp = Stonks()
    tmp.exchange_rate = 1.0
    tmp.main_site = 'main'

    mock = Mock()
    mock.text = '10'

    row = [[{'href': '!'}], mock, [0, 0, mock]]
    tmp.parse_initial_info(row)
    assert tmp.companies[0].url == 'main!'
    assert tmp.companies[0].latest_price == 10.0
    assert tmp.companies[0].year_growth == 1.0


def test_parse_company_details():
    tmp = Stonks()
    tmp.exchange_rate = 1.0
    mock1 = MagicMock()
    mock1[0].text = '335'
    mock1[0][0].text = '10'

    mock = MagicMock()
    mock.xpath = lambda _: mock1

    with patch('homework10.stonks.Stonks.request_contents', return_value=''), \
         patch('lxml.html.fromstring', return_value=mock):
        cmp = Mock()
        tmp.parse_company_details(cmp)
        assert cmp.name == '335'
        assert cmp.company_code == '5'
        assert cmp.high_low_diff == 100.0
        assert cmp.p_e == 335.0
