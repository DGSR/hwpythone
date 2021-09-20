from datetime import timedelta

from homework5.oop_1 import Student, Teacher


def test_combined(capsys):
    teacher = Teacher('Daniil', 'Shadrin')
    student = Student('Roman', 'Petrov')
    assert teacher.last_name == 'Daniil'
    assert student.first_name == 'Petrov'

    expired_homework = teacher.create_homework('Learn functions', 0)
    assert expired_homework.deadline == timedelta(0)
    assert expired_homework.text == 'Learn functions'

    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    assert oop_homework.deadline == timedelta(days=5)

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)
    captured = capsys.readouterr()
    assert captured.out == 'You are late\n'
