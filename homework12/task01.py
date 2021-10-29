from typing import Tuple

from sqlalchemy import Column, DateTime, Integer, String, create_engine, insert
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()


class Student(Base):
    """
    class represents student with last and first names
    """
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(25), nullable=False)
    last_name = Column(String(25), nullable=False)


class Teacher(Base):
    """
    class represents teacher with last and first names
    """
    __tablename__ = 'teacher'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(25), nullable=False)
    last_name = Column(String(25), nullable=False)


class Homework(Base):
    """
    class represents homework with text task and deadline attributes
    """
    __tablename__ = 'homework'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    created = Column(DateTime(timezone=True), server_default=func.now())
    deadline = Column(Integer, nullable=False)
    teacher = Column(Integer, ForeignKey('teacher.id'), nullable=False)


class HomeworkResult(Base):
    """
    class represents solution of homework with Homework object
    solution, author and created attributes
    """
    __tablename__ = 'homework_result'

    id = Column(Integer, primary_key=True)
    author = Column(Integer, ForeignKey('student.id'), nullable=False)
    created = Column(DateTime(timezone=True), server_default=func.now())
    homework = Column(Integer, ForeignKey('homework.id'), nullable=False)
    solution = Column(String, nullable=False)


class DB_main:
    """
    class for creating sqlite database and seeding it with data
    tables are classes inherited from Base
    has dump functions for creating and inserting
    """
    def __init__(self, engine: str = 'sqlite:///main.db'):
        self.engine = create_engine(engine)
        Base.metadata.drop_all(bind=self.engine)
        Base.metadata.create_all(self.engine)
        self.database_struct_dump()

    def database_struct_dump(self, filename: str = 'db_dump.txt') -> None:
        """
        dump database to given file
        """
        con = self.engine.raw_connection()
        with open(filename, 'w') as file:
            [file.write(str(line)+'\n') for line in con.iterdump()]
        con.close()

    def seed_db(self) -> None:
        """
        seed database with values and make a migration files out of it
        """
        std_1 = (insert(Student).values(first_name='Ivan', last_name='Ivanov'))
        std_2 = (insert(Student).values(first_name='John', last_name='Smith'))
        teacher = (insert(Teacher).values(first_name='Werner',
                                          last_name='Heisenberg'))
        hw_1 = (insert(Homework).values(text='compose rust', deadline=1,
                                             teacher=1))
        hw_2 = (insert(Homework).values(text='make a breakthrough',
                                             deadline=999, teacher=1))
        hw_res_1 = (insert(HomeworkResult).values(author=1, homework=1,
                                                  solution='just wait'))
        hw_res_2 = insert(HomeworkResult).values(author=2, homework=1,
                                                 solution='add iron to water')
        comp = {"literal_binds": True}
        raw_sql_std_1 = std_1.compile(self.engine, compile_kwargs=comp)
        raw_sql_std_2 = std_2.compile(self.engine, compile_kwargs=comp)
        raw_sql_teacher = teacher.compile(self.engine, compile_kwargs=comp)
        raw_sql_hw_1 = hw_1.compile(self.engine, compile_kwargs=comp)
        raw_sql_hw_2 = hw_2.compile(self.engine, compile_kwargs=comp)
        raw_sql_hw_res_1 = hw_res_1.compile(self.engine, compile_kwargs=comp)
        raw_sql_hw_res_2 = hw_res_2.compile(self.engine, compile_kwargs=comp)
        statements = (raw_sql_std_1, raw_sql_std_2, raw_sql_teacher,
                      raw_sql_hw_1, raw_sql_hw_2, raw_sql_hw_res_1,
                      raw_sql_hw_res_2)
        self.data_dump(*statements)
        [self.engine.execute(stmt) for stmt in statements]

    def data_dump(self, *lines: Tuple[str],
                  filename: str = 'data_dump.txt') -> None:
        """
        write string lines to given file
        """
        with open(filename, 'w') as file:
            [file.write(str(line)+';\n') for line in lines]
