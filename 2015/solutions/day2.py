file = open("2015/inputs/day2.txt", "r")
input = file.read()
if input[-1] == "\n":
    input = input[:-1]
file.close()

# Part 1
# formula for surface area: 2*l*w + 2*w*h + 2*h*l
total = 0

# create a list of all the dimensions splited by \n
dimensions = input.split("\n")
for i in range(len(dimensions)):
    dimensions[i] = dimensions[i].split("x")

# calculate the surface area for each box
for i in range(len(dimensions)):
    print(dimensions[i])
    l = int(dimensions[i][0])
    w = int(dimensions[i][1])
    h = int(dimensions[i][2])
    total += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
print("Total square feet of wrapping paper: " + str(total))

# Part 2
# formula for ribbon: 2*min(l+w, w+h, h+l) + l*w*h
total = 0
for i in range(len(dimensions)):
    l = int(dimensions[i][0])
    w = int(dimensions[i][1])
    h = int(dimensions[i][2])
    total += 2*min(l+w, w+h, h+l) + l*w*h
print("Total feet of ribbon: " + str(total))