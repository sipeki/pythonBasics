class Student:

    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def score(self, m1, m2, m3):
        # sumofnumbers = 0
        # for t in num:
          #  sumofnumbers = sumofnumbers + t

        # avg = sumofnumbers / len(num)
        return self.name + " your average score for " + self.subject + " " + str(int((m1+m2+m3)/3))



John = Student("John", "31", "maths")
Jane = Student("Jane", "24", "english")


print(Jane.score(23,45,67))

