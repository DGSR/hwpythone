from unittest.mock import Mock, patch

import pytest
import requests  # noqa: F401

from homework4.task2 import count_dots_on_i


def test_count_dots_on_i_positive():
    test_value = Mock()
    test_value.content = ("i" * 59).encode()
    with patch('requests.get', return_value=test_value):
        assert count_dots_on_i("https://example.com/") == 59


def test_count_dots_on_i_negative():
    with pytest.raises(ValueError):
        count_dots_on_i("https://www.nonexistingwebsite.com/")
