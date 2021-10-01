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

    def calc_avg(self):
        sum = 0
        quantity = 0
        average = 0
        for val in self.grades.values():
            for grade in val:
                sum += grade
                quantity += 1
                average = sum / quantity
        return round(average, 2)

    def __str__(self):
        return f"\n Имя: {self.name} \n Фамилия: {self.surname} \n Курсы в процессе изучения: {self.courses_in_progress} \n Завершенные курсы: {self.finished_courses} \n Средняя оценка за лекции: {self.calc_avg()}"


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
        average = 0
        for val in self.grades.values():
            for grade in val:
                sum += grade
                quantity += 1
                average = sum / quantity
        return round(average, 2)

    def __str__(self):
        return f"\n Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за лекции: {self.calc_avg()}"

    def calc_avg_lect(self, name, course):
        sum = 0
        quantity = 0
        average = 0
        if course in name.courses_attached:
             for course in name.grades.keys():
                for val in name.grades.values():
                    for grade in val:
                        sum += grade
                        quantity += 1
                        average = sum / quantity
             return print(round(average, 2))


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

    def __str__(self):
        return f"\n Имя: {self.name} \n Фамилия: {self.surname}"


ruoy = Student('Ruoy', 'Eman', 'our_gender')
ruoy.courses_in_progress += ['Python', 'Введение в программирование']
ruoy.finished_courses += ['Git']

moris = Student('Mrs', 'Moris', 'our_gender')
moris.courses_in_progress += ['Git']
moris.finished_courses += ['Введение в программирование']

some = Reviewer('Some', 'Buddy')
some.courses_attached += ['Python']

some.rate_hw(ruoy, 'Python', 10)
some.rate_hw(ruoy, 'Python', 9)
some.rate_hw(moris, 'Python', 9)
some.rate_hw(moris, 'Python', 9)

tony = Lecturer('Tony', 'Stark')
tony.courses_attached += ['Введение в программирование']
tony.courses_attached += ['Git']

ruoy.rate_hw_avg(tony, 'Введение в программирование', 8)
ruoy.rate_hw_avg(tony, 'Введение в программирование', 7)
ruoy.rate_hw_avg(tony, 'Git', 10)

thor = Lecturer('Thor', 'Simpson')
thor.courses_attached += ['Git']

moris.rate_hw_avg(thor, 'Git', 10)
moris.rate_hw_avg(thor, 'Git', 7)

def chec_avg(l_1, l_2):
    if l_1.calc_avg() > l_2.calc_avg():
        print(f'{l_1.name} {l_1.surname} лучше')
    elif l_1.calc_avg() < l_2.calc_avg():
        print(f'{l_2.name} {l_2.surname} лучше')
    else:
        print(f'они равны')

all_lectors = [tony, thor]

all_students = [ruoy, moris]

def calc_avg_lect(alect, acourse):
    sum = 0
    quantity = 0
    average = 0
    for l in alect:
      if acourse in l.courses_attached:
        for course in l.grades.keys():
          if acourse == course:
            for val in l.grades[course]:
                sum += val
                quantity += 1
    average = sum / quantity
    return print(f'Средний балл по преподавателям на курсе {acourse}: {round(average, 2)}')

calc_avg_lect(all_lectors, 'Git')

def calc_avg_stud(astud, acourse):
    sum = 0
    quantity = 0
    average = 0
    for s in astud:
      if acourse in s.courses_in_progress:
        for course in s.grades.keys():
          if acourse == course:
            for val in s.grades[course]:
                sum += val
                quantity += 1
    average = sum / quantity
    return print(f'Средний балл по студентам на курсе {acourse}: {round(average, 2)}')

calc_avg_stud(all_students, 'Python')

chec_avg(ruoy, moris)

print(ruoy)

print(tony)

print(some)

