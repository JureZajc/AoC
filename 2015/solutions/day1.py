import os

file = open(os.path.dirname(__file__) + "/../inputs/day1.txt", "r")
input = file.read()
file.close()

# Part 1
floor = 0
for i in input:
    if i == "(":
        floor += 1
    elif i == ")":
        floor -= 1
print("Santa is on floor: " + str(floor))

# Part 2
floor = 0
for i in range(len(input)):
    if input[i] == "(":
        floor += 1
    elif input[i] == ")":
        floor -= 1
    if floor == -1:
        basement = i + 1
        break
print("Basement is reached at position: " + str(basement))