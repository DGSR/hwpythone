import sys


def my_precious_logger(text: str) -> None:
    """
    prints to stderr if text starts with error otherwise to stdout
    """
    print(text, file=sys.stderr if text.startswith("error") else sys.stdout)
