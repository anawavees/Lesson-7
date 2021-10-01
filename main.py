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


best_student = Student('Ruoy', 'Eman', 'our_gender')
best_student.courses_in_progress += ['Python', 'Введение в программирование']
best_student.finished_courses += ['Git']

best_student_1 = Student('Mrs', 'Moris', 'our_gender')
best_student_1.courses_in_progress += ['Git']
best_student_1.finished_courses += ['Введение в программирование']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 7)
cool_mentor.rate_hw(best_student_1, 'Python', 9)
cool_mentor.rate_hw(best_student_1, 'Python', 9)

cool_lector = Lecturer('Tony', 'Stark')
cool_lector.courses_attached += ['Введение в программирование']
cool_lector.courses_attached += ['Git']

best_student.rate_hw_avg(cool_lector, 'Введение в программирование', 8)
best_student.rate_hw_avg(cool_lector, 'Введение в программирование', 7)
best_student.rate_hw_avg(cool_lector, 'Git', 10)

cool_lector_1 = Lecturer('Thor', 'Simpson')
cool_lector_1.courses_attached += ['Git']

best_student_1.rate_hw_avg(cool_lector_1, 'Git', 10)
best_student_1.rate_hw_avg(cool_lector_1, 'Git', 10)

# print(cool_lector.grades)
#
# print(cool_lector_1.grades)
#
# print(cool_lector.calc_avg())
#
# print(cool_lector_1.calc_avg())

def chec_avg(l_1, l_2):
    if l_1.calc_avg() > l_2.calc_avg():
        print(f'{l_1.name} {l_1.surname} лучше')
    elif l_1.calc_avg() < l_2.calc_avg():
        print(f'{l_2.name} {l_2.surname} лучше')
    else:
        print(f'они равны')

# def calc_avg_lect(Lecturer, course):
#     sum = 0
#     quantity = 0
#     average = 0
#     if course in Lecturer.courses_attached:
#          for course in Lecturer.grades.keys():
#              for val in Lecturer.grades.values():
#                     for grade in val:
#                      sum += grade
#                      quantity += 1
#                      average = sum / quantity
#              return print(round(average, 2))

AllLectors = [cool_lector, cool_lector_1]
print(AllLectors)

def calc_avg_lect(ALect, ACourse):
    sum = 0
    quantity = 0
    average = 0
    #Lecturer.__init__()
    for L in ALect:
      if ACourse in L.courses_attached:
        for course in L.grades.keys():
          if ACourse == course:
            #print(course)
            for val in L.grades[course]:
              #for grade in val:
                #print(val)
                sum += val
                quantity += 1
                average = sum / quantity
    return print(round(average, 2))

calc_avg_lect(AllLectors, 'Git')

# chec_avg(cool_lector, cool_lector_1)

# print(best_student.grades)
#
# print(best_student.calc_avg())

chec_avg(best_student, best_student_1)

print(best_student)

print(cool_lector)

print(cool_mentor)

