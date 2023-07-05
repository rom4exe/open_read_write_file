class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_ment(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self) -> str:
        if self.finished_courses:
            fin = ", ".join(self.finished_courses)
        else:
            fin = "отсутствуют"
        return f'имя: {self.name}\nфамилия: {self.surname}\n\
Средняя оценка за домашние задания: {Averaged(self)}\nКурсы в процессе изучения: \
{", ".join(self.courses_in_progress)}\nЗавершенные курсы: {fin}\n'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'сравнение возможно только одной грыппы: или преподователей или студентов')
            return
        return Averaged(self) < Averaged(other)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self) -> str:
        return f'имя: {self.name}\nфамилия: {self.surname}\nСредняя оценка за лекции: {Averaged(self)}\n'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'сравнение возможно только одной грыппы: или преподователей или студентов')
            return
        return Averaged(self) < Averaged(other)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self) -> str:
        return f'имя: {self.name}\nфамилия: {self.surname}\n'


def Averaged(self):
    a = 0
    b = 0
    if self.grades:
        for i in self.grades.values():
            for j in i:
                a += 1
                b += j
        return b / a
    else:
        return "Оценок нет"


def Aver_course(list_any, course):
    a = 0
    l = 0
    for std in list_any:
        if course in std.grades.keys():
            sred_ed = (sum(std.grades[course])) / (len(std.grades[course]))
            a += 1
            l += sred_ed
        else:
            continue
    return (course, l / a)


best_student1 = Student('Ruoy', 'Eman', 'm')
best_student1.courses_in_progress += ['Python']

best_student2 = Student('Ivan', 'Petrov', 'm')
best_student2.courses_in_progress += ['Python', 'Java']
best_student2.finished_courses += ['Delphi']

lecturer1 = Lecturer('Петр', 'Филипов')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Геннадий', 'Аффанасьев')
lecturer2.courses_attached += ['Python', 'Java']

reviewer1 = Reviewer('Василий', 'Парфёнов')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Евгений', 'Тодоренко')
reviewer2.courses_attached += ['Java']

reviewer1.rate_hw(best_student1, 'Python', 10)
reviewer1.rate_hw(best_student1, 'Python', 6)
reviewer1.rate_hw(best_student2, 'Python', 8)
reviewer2.rate_hw(best_student2, 'Java', 7)

best_student1.rate_ment(lecturer1, 'Python', 9)
best_student2.rate_ment(lecturer1, 'Python', 7)
best_student2.rate_ment(lecturer2, 'Java', 10)
best_student2.rate_ment(lecturer2, 'Python', 7)

list_lecturers = [lecturer1, lecturer2]
list_students = [best_student1, best_student2]

print(best_student1)
print(best_student2)

print(lecturer1)
print(lecturer2)

print(reviewer1)

print(best_student1 < best_student2)
print(lecturer1 > lecturer2)
print(lecturer1 > best_student1)

stud_aver = Aver_course(list_students, 'Python')
stud_aver2 = Aver_course(list_students, 'Java')
lect_aver = Aver_course(list_lecturers, 'Java')
lect_aver2 = Aver_course(list_lecturers, 'Python')

print(f"средняя оценка по всем студентам курса {stud_aver[0]}: {stud_aver[1]}")
print(f"средняя оценка по всем студентам курса {stud_aver2[0]}: {stud_aver2[1]}")
print(f"средняя оценка по всем лекторам курса {lect_aver[0]}: {lect_aver[1]}")
print(f"средняя оценка по всем лекторам курса {lect_aver2[0]}: {lect_aver2[1]}")