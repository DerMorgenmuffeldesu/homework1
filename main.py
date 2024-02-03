class Student:
  def __init__(self, name, surname, gender):
    self.name = name
    self.surname = surname
    self.gender = gender
    self.finished_courses = []
    self.courses_in_progress = []
    self.grades = {}

  def rate_lecturer(self, lecturer, course, grade):
    if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
      if course in lecturer.grades:
        lecturer.grades[course] += [grade]
      else:
        lecturer.grades[course] = [grade]
    else:
      return 'Ошибка'
    # print(lecturer.grades)
  
  # def av_rate_lec():
  #   for key, value in lecturer.grades:
  #     print(value)
  #   return "ddf"
  
  # def __str__(self):
  #   Student.av_rate_lec()
  #   return (f"Имя: {self.name}\nФамилия: {self.surname}")

class Mentor:
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.courses_attached = []
  
  def __str__(self):
    return (f"Имя: {self.name}\nФамилия: {self.surname}")   

class Lecturer(Mentor):
  grades = {}
      
class Reviewer(Mentor):
  def rate_homework(self, student, course, grade):
    if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
      if course in student.grades:
        student.grades[course] += [grade]
      else:
        student.grades[course] = [grade]
    else:
      return 'Ошибка'



student_1 = Student('Сергей', 'Иванов', 'M')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['PHP']
student_1.courses_in_progress += ['C++']

reviewer_1 = Reviewer('Петр', 'Яковлев')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['C++']
reviewer_1.courses_attached += ['PHP']
print(f'Проверяющий: {reviewer_1.name} {reviewer_1.surname}\nВедёт курсы: {" ".join(reviewer_1.courses_attached)}\n')

reviewer_1.rate_homework(student_1, 'Python', 10)
reviewer_1.rate_homework(student_1, 'C++', 4)
reviewer_1.rate_homework(student_1, 'PHP', 6)
print(f'Оценки студента: {student_1.name} {student_1.surname}\n{student_1.grades}')
print("-----------------\n")

lecturer_1 = Lecturer('Никита', 'Сидоров')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['PHP']
lecturer_1.courses_attached += ['C++']

student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_1, 'PHP', 5)
student_1.rate_lecturer(lecturer_1, 'C++', 3)
print(f'Оценки лектору: {lecturer_1.name} {lecturer_1.surname}\n{lecturer_1.grades}')
print("-----------------\n")

print(student_1)

print(reviewer_1)

print(lecturer_1)




# class Reviewer(Mentor):
    
#     def rate_hw(self, student, course, grade):
#         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
#             if course in student.grades:
#                 student.grades[course] += [grade]
#             else:
#                 student.grades[course] = [grade]
#         else:
#             return 'Ошибка'
        
 
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
 
# cool_reviewer = Reviewer('Some', 'Buddy')
# cool_reviewer.courses_attached += ['Python']
 
# cool_reviewer.rate_hw(best_student, 'Python', 10)
# cool_reviewer.rate_hw(best_student, 'Python', 10)
# cool_reviewer.rate_hw(best_student, 'Python', 10)
 
# print(best_student.grades)