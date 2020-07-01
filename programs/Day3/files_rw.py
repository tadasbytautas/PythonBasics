file = open("teams.txt", "w")
for team in range(1,5):
    newteam = "This is team " + str(team) + "\n"
    file.write(newteam)

file.close()

file = open("teams.txt", "r")
print(file.readline())
file.readline()
file.readline()
print(file.readline())

file.close()

file = open("teams.txt", "w")
newline = file.write(str("This is a new line"))

print(newline)
