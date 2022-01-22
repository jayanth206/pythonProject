class Student:
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # setter method(mutator)
    def set(self):
        m1 = 85

    # getter method(accessor)
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3


s1 = Student(84, 77, 90)
s2 = Student(30, 70, 90)
s1.set()
print(s1.avg())
print(s2.avg())