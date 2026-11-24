class Person:
    def __init__(self, name, email):
        self._name = name
        self._email = email

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email


class Course:
    def __init__(self, code, title, credits):
        self.__code = code
        self.__title = title
        self.__credits = credits

    def get_code(self):
        return self.__code

    def get_title(self):
        return self.__title

    def get_credits(self):
        return self.__credits

    def __str__(self):
        return f"{self.__code} - {self.__title} ({self.__credits} cr)"


class Student(Person):
    def __init__(self, student_id, name, email, department):
        super().__init__(name, email)
        self.__student_id = student_id
        self.__department = department
        self.__gpa = 0.0
        self.__courses = []

    def get_student_id(self):
        return self.__student_id

    def get_department(self):
        return self.__department

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        if 0.0 <= gpa <= 4.0:
            self.__gpa = gpa
        else:
            print("GPA must be between 0.0 and 4.0")

    def enroll(self, course):
        if course not in self.__courses:
            self.__courses.append(course)

    def drop(self, course):
        if course in self.__courses:
            self.__courses.remove(course)

    def get_courses(self):
        return self.__courses

    def show_info(self):
        print(f"ID: {self.__student_id} | {self._name} ({self._email})")
        print(f"Department: {self.__department} | GPA: {self.__gpa}")
        print("Courses:")
        for c in self.__courses:
            print(f"  - {c}")
