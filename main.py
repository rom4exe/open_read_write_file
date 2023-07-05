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

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)
