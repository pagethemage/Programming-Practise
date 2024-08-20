class Student:
    def __init__(self, name, age, grade):
        self.name:str = name
        self.age:int = age
        self.grade:int = grade

    def get_grade(self):
        return self.grade
    
    def __str__(self):
        return (f"{self.name} {self.age} {self.grade}")
    
class Course:
    def __init__(self, name, max_students):
        self.name:str = name
        self.max_students:int = max_students
        self.students:list = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return (value / len(self.students))
    
    def print_students(self):
        print("\n")
        for index, x in enumerate(self.students, start = 1):
            print(f"{index}: {x}")


s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)


course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.add_student(s3))
print(f"Average grade: {course.get_average_grade()}")   
print(course.print_students())