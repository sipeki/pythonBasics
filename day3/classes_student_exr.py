class Student:

    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def score(self, m1, m2, m3):
        print("Your score for " + self.subject + " " + ((m1+m2+m3)/3))
        return



print("m1")

John = Student("John", "31", "maths")
Jane = Student("Jane", "24", "english")


print(Jane.score(23,45,67))

