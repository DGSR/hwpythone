from collections import defaultdict
from datetime import datetime, timedelta


class DeadlineError(Exception):
    pass


class Homework:
    """
    class represents homework with text task and deadline attributes
    """
    def __init__(self, text: str, deadline: int):
        self.text = text
        self.deadline = timedelta(days=deadline)
        self.created = datetime.now()

    def is_active(self) -> bool:
        """
        return True if deadline has not passed yet else False
        """
        return self.created + self.deadline > datetime.now()


class HomeworkResult:
    """
    class represents solution of homework with Homework object
    solution, author and created attributes
    """
    def __init__(self, homework: Homework, solution: str, student: 'Student'):
        if not isinstance(homework, Homework):
            raise ValueError("You gave a not Homework object")

        self.homework = homework
        self.solution = solution
        self.author = student
        self.created = datetime.now()


class Student:
    """
    class represents student with last and first names
    """
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, homework: Homework, solution: str) -> HomeworkResult:
        """
        return Homework object if deadline has not passed yet else raise error
        """
        if not homework.is_active():
            raise DeadlineError('You are late')

        return HomeworkResult(homework, solution, self)


class Teacher(Student):
    """
    class represents teacher with last and first names
    """
    homework_done = defaultdict(set)

    def check_homework(self, homework_result: HomeworkResult) -> bool:
        """
        returns True if solution of HomeworkResult is > 5 else False
        and adds HomeworkResult to homework_done dict
        """
        if len(homework_result.solution) < 5:
            return False

        self.homework_done[homework_result.homework].add(homework_result)
        return True

    @staticmethod
    def create_homework(text: str, deadline: timedelta) -> Homework:
        """
        static method, which returns Homework
        """
        return Homework(text, deadline)

    @staticmethod
    def reset_results(homework: Homework = None) -> None:
        """
        clear all results in homework_done by key homework
        if nothing passed clear homework_done
        """
        if not homework:
            Teacher.homework_done = defaultdict(set)

        Teacher.homework_done.clear()
