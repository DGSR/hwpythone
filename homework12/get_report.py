from sqlalchemy import create_engine, MetaData, select
import csv
from typing import List


def get_done_homework(db_uri: str) -> List:
    """
    connect to db and get data from 4 joined tables:
        teacher, student, homework, homework_result
    """
    engine = create_engine(db_uri)

    meta = MetaData()
    meta.reflect(bind=engine)

    teacher_t = meta.tables['teacher']
    student_t = meta.tables['student']
    hw_t = meta.tables['homework']
    hw_res_t = meta.tables['homework_result']

    conn = engine.connect()
    join_obj = hw_res_t.join(student_t, hw_res_t.c.author == student_t.c.id)\
                       .join(hw_t, hw_res_t.c.homework == hw_t.c.id)\
                       .join(teacher_t, hw_t.c.teacher == teacher_t.c.id)
    selected_cols = [hw_t.c.created, student_t.c.last_name,
                     teacher_t.c.last_name]
    sel_st = select(selected_cols).select_from(join_obj)
    res = []
    for elem in conn.execute(sel_st):
        res.append(elem)
    return res


def get_report(db_uri: str = 'sqlite:///main.db') -> None:
    """
    writes data from get_done_homework to report.csv
    """
    res = get_done_homework(db_uri)
    with open('report.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        [writer.writerow(elem) for elem in res]
