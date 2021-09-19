import sys


def my_precious_logger(text: str):
    print(text, file=sys.stderr if text.startswith("error") else sys.stdout)
