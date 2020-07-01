class students:
    name = "student"
    age = "student"
    school_class = "student"

    def __init__(self, name, age, school_class):
        self.name = name
        self.age = age
        self.school_class = school_class

    def calcAvgScore():
        test1 = int(input("test nr 1 score: "))
        test2 = int(input("test nr 2 score: "))
        test3 = int(input("test nr 3 score: "))
        total = (test1 + test2 + test3) / 3
        return total
        # print("Average score for tests is: " + str(total))

newStudent = students("Tadas", "33", "IT")

print(newStudent.name)
print(newStudent.age)
print(newStudent.school_class)

students.calcAvgScore()
