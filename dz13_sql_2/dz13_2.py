import sqlite3

SQLbaza=sqlite3.connect('mydatabase.db')
data=SQLbaza.cursor()

data.execute(f"""CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER,
grade TEXT
);""")
#PRIMARY KEY AUTOINCREMENT - автоматически увеличивает значение на единицу
def new_student():
    name=input('Введите имя ученика: ')
    age=int(input('Введите возраст ученика: '))
    grade=input('Введите оценку: ')
    data.execute(f"INSERT INTO students(name,age,grade) VALUES ('{name}','{age}','{grade}');")
def get_student_by_name():
    name=input('Введите имя студента о котором хотите узнать информацию: ')
    print(data.execute(f"SELECT * FROM students WHERE name='{name}' ;").fetchone())
def update_student_grade():
    name=input('Введите имя ученика, оценку которого хотите изменить: ')
    grade= input('Введите какую оценку хотите поставить ученику: ')
    data.execute(f"UPDATE students SET grade='{grade}' WHERE name='{name}'")
def delete_student():
    name=input('Введите имя ученика от которого хотите избавиться: ')
    data.execute(f"DELETE FROM students WHERE name='{name}'")
def info_student():
    print(data.execute(f"SELECT * FROM students").fetchall())
while True:
    print("1 - Добавление ученика")
    print("2 - Информация о студенте")
    print("3 - Добавить новую оценку")
    print("4 - Удалить от ученика")
    print("5 - Информация о всех учениках")
    action=int(input())
    if action==1:
        new_student()
        SQLbaza.commit()

    elif action==2:
        get_student_by_name()
        SQLbaza.commit()

    elif action==3:
        update_student_grade()
        SQLbaza.commit()

    elif action==4:
        delete_student()
        SQLbaza.commit()

    elif action==5:
        info_student()
        SQLbaza.commit()

    elif action==6:
        SQLbaza.close()
        break
