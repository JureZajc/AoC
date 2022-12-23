import os
file = open(os.path.dirname(__file__) + "/../inputs/day6.txt", "r")
lines = file.readlines()
if lines[-1] == "\n":
    lines = lines[:-1]
file.close()

# Part 1
# Create a 1000x1000 grid of lights
lights = [[0 for x in range(1000)] for y in range(1000)]

for item in lines:
    # Split the line into its components
    line = item.split(" ")

    # Get the start and end coordinates
    start = line[-3].split(",")
    end = line[-1].split(",")
    start = [int(start[0]), int(start[1])]
    end = [int(end[0]), int(end[1])]

    # Turn on the lights
    if line[0] == "turn":
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                if line[1] == "on":
                    lights[x][y] = 1
                else:
                    lights[x][y] = 0
    # Toggle the lights
    else:
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                lights[x][y] = 1 - lights[x][y]

# Count the number of lights that are on
count = 0
for x in range(1000):
    for y in range(1000):
        count += lights[x][y]
    
print("Part 1:", count)

# Part 2

lights = [[0 for x in range(1000)] for y in range(1000)]
brightness = 0

for item in lines:
    # Split the line into its components
    line = item.split(" ")

    # Get the start and end coordinates
    start = line[-3].split(",")
    end = line[-1].split(",")
    start = [int(start[0]), int(start[1])]
    end = [int(end[0]), int(end[1])]

    # Turn on the lights
    if line[0] == "turn":
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                if line[1] == "on":
                    lights[x][y] += 1
                else:
                    lights[x][y] -= 1
                    if lights[x][y] < 0:
                        lights[x][y] = 0
    # Toggle the lights
    else:
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                lights[x][y] += 2
print("Part 2:", sum(sum(lights, [])))