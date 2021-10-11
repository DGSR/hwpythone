import contextlib
import sqlite3
from constant.sql_queries import (SELECT_COUNT_FROM_PARAMETERIZED,
                                  SELECT_FROM_PARAMETERIZED,
                                  SELECT_FROM_WHERE_PARAMETERIZED)


def TableDataCollection(cls):
    """
    decorator which acts as a collection object based on decorated class
    overrides __len__, __getitem__, __contains__, __iter__
     with methods of decorated class
    """
    class Wrapper():
        def __init__(self, database, table) -> None:
            self.__db__ = cls(database, table)

        def __len__(self) -> int:
            return self.__db__.get_rows_number()

        def __getitem__(self, item: str):
            return self.__db__.get_row_by_name(item)

        def __contains__(self, item: str):
            return self.__db__.row_exists(item)

        def __iter__(self):
            return self.__db__.iterator()
    return Wrapper


@contextlib.contextmanager
def db_connect(database):
    """
    context manager for DB sqlite
    accepts database as argument
    """
    db_connection = sqlite3.connect(database)
    try:
        yield db_connection
    finally:
        db_connection.close()


@TableDataCollection
class TableData:
    """
    class accepts database and table as arguments
    and provides functionality with database
    """
    def __init__(self, database_name: str, table_name: str):
        self.database_name = database_name
        self.table_name = table_name

    def get_rows_number(self) -> int:
        """
        return number of rows in database.table defined by class
        """
        with db_connect(self.database_name) as conn:
            cursor = conn.cursor()
            query = SELECT_COUNT_FROM_PARAMETERIZED % (self.table_name)
            cursor.execute(query)
            return cursor.fetchone()[0]

    def get_row_by_name(self, name):
        """
        return row where name == argument in database.table defined by class
        """
        with db_connect(self.database_name) as conn:
            cursor = conn.cursor()
            query = SELECT_FROM_WHERE_PARAMETERIZED % (self.table_name)
            cursor.execute(query, {'name': name})
            return cursor.fetchone()

    def row_exists(self, name):
        """
        return if name is in database.table defined by class
        """
        with db_connect(self.database_name) as conn:
            cursor = conn.cursor()
            query = SELECT_FROM_PARAMETERIZED % (self.table_name)
            for row in cursor.execute(query):
                if name in row:
                    return True
            return False

    def iterator(self):
        """
        yields row in database.table defined by class
        """
        with db_connect(self.database_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            query = SELECT_FROM_PARAMETERIZED % (self.table_name)
            cursor.execute(query)
            while row := cursor.fetchone():
                yield row
