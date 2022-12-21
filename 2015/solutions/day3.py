import os

file = open(os.path.dirname(__file__) + "/../inputs/day3.txt", "r")
input = file.read()
if input[-1] == "\n":
    input = input[:-1]
file.close()

# Part 1
houses = set()
directions = "^v<>"
x = 0
y = 0
houses.add((x, y))
for direction in input:
    if direction == directions[0]:
        y += 1
    elif direction == directions[1]:
        y -= 1
    elif direction == directions[2]:
        x -= 1
    elif direction == directions[3]:
        x += 1
    houses.add((x, y))
print("Houses visited: " + str(len(houses)))

# Part 2
houses = set()
directions = "^v<>"
x = [0, 0]
y = [0, 0]
houses.add((x[0], y[0]))
for i in range(len(input)):
    if input[i] == directions[0]:
        # add to y depending on which santa is moving
        y[i % 2] += 1
    elif input[i] == directions[1]:
        y[i % 2] -= 1
    elif input[i] == directions[2]:
        x[i % 2] -= 1
    elif input[i] == directions[3]:
        x[i % 2] += 1
    houses.add((x[i % 2], y[i % 2]))
print("Houses visited: " + str(len(houses)))