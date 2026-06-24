import random

class Animal:
    def __init__(self, legs, color, offspring_count, name):
        self.legs = legs
        self.color = color
        self.offspring_count = offspring_count
        self.name = name
        self.tail = None

    def add_tail(self, tail_object):
        self.tail = tail_object

class Tail:
    def __init__(self, len, thickness, speed):
        self.len = len
        self.thickness = thickness
        self.speed = speed

class Cat(Animal):
    def __init__(self, color, name):
        self.whiskers = None
        self.mice_counter = 0
        super().__init__(legs=4, color=color, offspring_count=40, name=name)

    def hunt_mouse(self):
        self.mice_counter += 1

    def get_hunted_mice(self):
        return self.mice_counter

    def add_whiskers(self, whiskers):
        self.whiskers = whiskers

my_cat = Cat("purple", "shimy")
cat_tail = Tail(len=20, thickness=3, speed=5)
my_cat.add_tail(cat_tail)

print(f"אורך הזנב של {my_cat.name} הוא: {my_cat.tail.len} ס''מ.")
print(f"מספר העכברים ש-{my_cat.name} צד עד היום: {my_cat.mice_counter}")









