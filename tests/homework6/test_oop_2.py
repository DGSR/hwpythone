from collections import defaultdict

import pytest

from homework6.oop_2 import DeadlineError, HomeworkResult, Student, Teacher


def test_combined():
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)
    assert isinstance(good_student.do_homework(oop_hw, ''),
                      HomeworkResult) is True
    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')

    assert opp_teacher.check_homework(result_1) is True
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    assert opp_teacher.check_homework(result_3) is False

    Teacher.reset_results()
    assert Teacher.homework_done == defaultdict(set)

    late_hw = Teacher.create_homework("", -1)
    with pytest.raises(DeadlineError):
        lazy_student.do_homework(late_hw, '')
