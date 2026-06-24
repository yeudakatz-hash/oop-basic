from oop1 import Person

class Students(Person):
    def __init__(self, name, age, city, student_id, grade):
        super().__init__(name=name, age=age, city=city)
        self.student_id = student_id
        self.grade = grade

    def study(self):
        print(f"{self.name} לומד בשכבה {self.grade}")

    def introduce(self):
        print(f" {self.name}, בן {self.age} מ{self.city}, לומד בשכבה {self.grade}")

    def advance_grade(self):
        self.grade += 1
        print(f"{self.name} עלה לכיתה {self.grade}")

class Teacher(Person):
    def __init__(self, name, age, city, subject, years_experience):
        super().__init__(name=name, age=age, city=city)
        self.subject = subject
        self.years_experience = years_experience

    def teach(self):
        print(f"{self.name} מלמד {self.subject} כבר {self.years_experience} שנים")

    def introduce(self):
        print(f" {self.name}, מלמד {self.subject} כבר {self.years_experience}")

    def gain_experience(self):
        self.years_experience += 1
        print(f"הניסיון של המורה {self.name} גדל ל-{self.years_experience} שנים")

class Principal(Person):
    def __init__(self, name, age, city, years_as_principal):
        super().__init__(name=name, age=age, city=city)
        self.years_as_principal = years_as_principal

    def manage(self):
        print(f"{self.name} מנהל את המוסד כבר {self.years_as_principal} שנים")

    def introduce(self):
        print(f"שלום, אני {self.name}, בן/בת {self.age} מ{self.city}, מנהל המוסד")

    def add_management_experience(self):
        self.years_as_principal += 1
        print(f"הניסיון הניהולי של {self.name} גדל ל-{self.years_as_principal} שנים")

student1 = Students("יוסף", 3, "יבנה", "123", 9)
teacher1 = Teacher("דן", 40, "ספסל", "מתמטיקה", 10)
principal1 = Principal("אברהם", 55, "ברחוב", 8)

student1.introduce()
teacher1.introduce()
principal1.introduce()

student1.study()
teacher1.teach()
principal1.manage()

student1.advance_grade()
teacher1.gain_experience()
principal1.add_management_experience()


student1.introduce()
teacher1.introduce()
principal1.introduce()
