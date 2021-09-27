class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw_avg(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def calc_avg(self):
        sum = 0
        quantity = 0
        for val in self.grades.values():
            for grade in val:
                sum += grade
                quantity += 1
                average = sum / quantity
        return average

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'our_gender')
best_student.courses_in_progress += ['Python', 'Введение в программирование']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 7)
cool_mentor.rate_hw(best_student, 'Python', 9)

cool_lector = Lecturer('Tony', 'Stark')
cool_lector.courses_attached += ['Введение в программирование']

best_student.rate_hw_avg(cool_lector, 'Введение в программирование', 8)
best_student.rate_hw_avg(cool_lector, 'Введение в программирование', 2)

print(cool_lector.grades)

print(cool_lector.calc_avg())

print(best_student.grades)