import random

students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}

for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(3)]
        students_marks[student][class_] = marks

for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Удалить данные по ученикам/предметам/оценкам
        5. Редактировать данные по ученикам/предметам/оценкам
        6. Вывести все оценки для определенного ученика
        7. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print(f'Список учеников: {students}')
        print('1. Добавить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        print(f'Список предметов: {classes}')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {round(marks_sum / marks_count, 2)}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('''
        Удалить данные по: 
        1. Ученикам
        2. Предметам
        3. Оценкам
        ''')
        command = int(input('Введите команду: '))
        if command == 1:
            print('1. Удалить ученика')
            print(f'Ученики: {students}')
            student = input('Введите имя ученика, которого хотите удалить: ')
            if student in students:
                students.remove(student)
                print(f'Ученик {student} удален из списка учеников: ')
                print(f'Список учеников: {students}')
            else:
                print('Такого ученика не сущетсвует')
        if command == 2:
            print('2. Удалить предмет')
            print(f'Предметы: {classes}')
            class_ = input('Введите название предмета, который хотите удалить: ')
            if class_ in classes:
                classes.remove(class_)
                print(f'Предмет {class_} удален из списка предметов: ')
                print(f'Список предметов: {classes}')
            else:
                print('Такого предмета не сущетсвует')
        if command == 3:
            print('3. Удалить оценку')
            print(f'Ученики: {students}')
            student = input('Введите имя ученика, у которого вы хотите удалить оценку: ')
            print(f'Предметы: {classes}')
            class_ = input('Введите название предмета, по которому вы хотите удалить оценку: ')
            print(f'Оценки ученика {student} по предмету {class_}: {students_marks[student][class_]}')
            mark = int(input('Введите оценку, которую хотите удалить: '))
            if student in students and class_ in classes and mark in students_marks[student][class_]:
                students_marks[student][class_].remove(mark)
                print(f'Текущие оценки ученика {student} по предмету {class_}: {students_marks[student][class_]}')
            else:
                print('Ошибка! Такого ученика/предмета/оценки не сущетсвует!')

    elif command == 5:
        print('''
        Редактировать данные по: 
        1. Ученикам
        2. Предметам
        3. Оценкам
        ''')
        command = int(input('Введите команду: '))
        if command == 1:
            print('1. Редактировать ученика')
            print(f'Ученики: {students}')
            student = input('Введите имя ученика, которого хотите отредактировать: ')
            if student in students:
                k = students.index(student)
                students[k] = input('Введите новое имя ученика: ')
                print(f'Список учеников: {students}')
            else:
                print('Такого ученика не существует')
        if command == 2:
            print('2. Редактировать предмет')
            print(f'Предметы: {classes}')
            class_ = input('Введите название предмета, который хотите отредактировать: ')
            if class_ in classes:
                k = classes.index(class_)
                classes[k] = input('Введите новое название предмета: ')
                print(f'Список предметов: {classes}')
            else:
                print('Такого предмета не сущетсвует')


    elif command == 6:
        print(f'Список учеников: {students}')
        student = input('Введите имя ученика для просмотра оценок: ')
        if student in students:
            print(f'6.Все оценки для ученика: {student}')
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
        else:
            print('Такого ученика не существует')
    elif command == 7:
        print('7. Выход из программы')
        break