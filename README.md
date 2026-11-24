# Student Class Diagram

Ahmet Atmaca - 20230526 (`20230526@std.neu.edu.tr`)

Mapping a simple student class diagram to python code for the Software Implementations assignment.

```mermaid
classDiagram
    class Person {
        #str name
        #str email
        +get_name() str
        +get_email() str
        +set_email(email)
    }

    class Student {
        -str student_id
        -str department
        -float gpa
        -list courses
        +get_student_id() str
        +get_department() str
        +get_gpa() float
        +set_gpa(gpa)
        +enroll(course)
        +drop(course)
        +get_courses() list
        +show_info()
    }

    class Course {
        -str code
        -str title
        -int credits
        +get_code() str
        +get_title() str
        +get_credits() int
    }

    Person <|-- Student
    Student "0..*" --> "0..*" Course : enrolls in
```

`Student` extends `Person` and keeps a list of `Course` objects. Protected fields use `_`, private fields use `__` with getters and setters.

To run:
```bash
python3 main.py
```
