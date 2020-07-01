def calcGrade():
    studenName = input("what is student name: ")
    hwMark = input("what is the " + studenName + " homework grade: ")
    assMark = input("what is the " + studenName + " assessment grade: ")
    exaMark = input("what is the " + studenName + " exam grade: ")
    totalperc = ((int(hwMark) + int(assMark) + int(exaMark)) / 175) * 100
    return studenName + " grade is " + str(totalperc)


print(calcGrade())
