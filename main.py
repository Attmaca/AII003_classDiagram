from student import Student, Course


se301 = Course("AII003", "Software Design", 4)
se304 = Course("AII001", "Database Systems", 3)
se312 = Course("AII002", "Software Testing", 3)

s1 = Student("20230526", "Ahmet Atmaca", "20230526@std.neu.edu.tr", "Software Engineering")
s1.enroll(se301)
s1.enroll(se304)
s1.enroll(se312)
s1.drop(se312)
s1.set_gpa(3.45)

s2 = Student("20230458", "xxx", "xxx@std.neu.edu.tr", "Software Engineering")
s2.enroll(se301)
s2.set_gpa(3.10)

s1.show_info()
print()
s2.show_info()
