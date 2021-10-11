from datetime import datetime, timedelta


class Homework:
    """class represents homework with text task and deadline attributes"""
    def __init__(self, text: str, deadline: int):
        self.text = text
        self.deadline = timedelta(days=deadline)
        self.created = datetime.now()

    def is_active(self) -> bool:
        """return True if deadline has not passed yet else False"""
        return self.created + self.deadline > datetime.now()


class Student:
    """class represents student with last and first names"""
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework: Homework) -> Homework:
        """return Homework object if deadline has not passed yet else None"""
        return homework if homework.is_active() else print('You are late')


class Teacher:
    """class represents teacher with last and first names"""
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def create_homework(text: str, deadline: timedelta) -> Homework:
        """static method, which returns Homework"""
        return Homework(text, deadline)
