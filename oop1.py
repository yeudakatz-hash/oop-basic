class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"שלום, אני {self.name} , בן{self.age} מ{self.city}")

    def have_birthday(self):
        self.age += 1
        print(f"יום הולדת שמח! עכשיו אני בן/בת {self.age}")

person1 = Person("יוסף", 3 , "יבנה")
person2 = Person("דן", 4 , "ספסל")
person3 = Person("ישראלי", 5 , "ברחוב")

person1.introduce()
person2.introduce()
person3.introduce()

person1.have_birthday()



class Mosad:
    def __init__(self, name, type, students_count, city):
        self.name = name
        self.type = type
        self.students_count = students_count
        self.city = city

    def print_details(self):
        print(f"מוסד: {self.name} | סוג: {self.type} | תלמידים: {self.students_count} | עיר: {self.city}")

    def add_students(self, students_count):
        self.students_count += students_count

    def remove_students(self, students_count):
        if self.students_count >= students_count:
            self.students_count -= students_count
        else:
            self.students_count = 0

school = Mosad("נועם", "בית ספר", 200, "פתח תקווה")
university = Mosad("הטכניון", "אוניברסיטה", 5000, "חיפה")

school.print_details()
university.print_details()

school.add_students(50)
university.remove_students(20)

school.print_details()
university.print_details()
