from typing import List, Union

from constant.constants import KEY_VALUE_SEPARATOR


def ValueStorageDecorator(cls):
    """
    decorator which extracts self.dict from class
    overrides __getitem__ and __getattr__
    to return values from self.dict
    """
    class Wrapper:
        def __init__(self, filepath) -> None:
            self.storage = cls(filepath).dict

        def __getitem__(self, item: str) -> Union[int, str]:
            """
            return value from storage dict by item
            """
            return self.storage[item]

        def __getattr__(self, item: str) -> Union[int, str]:
            """
            return value from storage dict by item
            """
            return self.storage[item]
    return Wrapper


@ValueStorageDecorator
class KeyValueStorage:
    """
    class receives file, where each line is key and value separated by divider
    class reads file and writes down contents into dictionary
    if index is not identifier ValueError raised
    """
    def __init__(self, filepath: str) -> dict:
        file = self.open_file(filepath)
        self.dict = dict(line.split(KEY_VALUE_SEPARATOR) for line in file)
        self.check_values_of_dict()

    def open_file(self, filepath: str) -> List[str]:
        """
        read and return list of lines in file
        """
        with open(filepath, 'r') as file:
            return file.read().splitlines()

    def check_values_of_dict(self) -> None:
        """
        check self.dict if keys are identifiers
         and converts values to integers
        """
        for index, value in self.dict.items():
            if not index.isidentifier():
                raise ValueError(f'Incorrect key {index}')
            self.dict[index] = int(value) if value.isnumeric() else value
