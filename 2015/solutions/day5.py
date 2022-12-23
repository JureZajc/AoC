import os

file = open(os.path.dirname(__file__) + "/../inputs/day5.txt", "r")
input = file.read()
if input[-1] == "\n":
    input = input[:-1]
file.close()

vowels = "aeiou"
notContains = ["ab", "cd", "pq", "xy"]
niceStrings = 0

for string in input.split("\n"):
    vowelCount = 0
    doubleLetter = False
    contains = False
    for i in range(len(string)):
        if string[i] in vowels:
            vowelCount += 1
        if i < len(string) - 1:
            if string[i] == string[i + 1]:
                doubleLetter = True
            if string[i:i + 2] in notContains:
                contains = True
    if vowelCount >= 3 and doubleLetter and not contains:
        niceStrings += 1
print("Nice strings: " + str(niceStrings))

# Part 2
niceStrings = 0
for string in input.split("\n"):
    doublePair = False
    repeatLetter = False
    for i in range(len(string)):
        if i < len(string) - 3:
            if string[i:i + 2] in string[i + 2:]:
                doublePair = True
        if i < len(string) - 2:
            if string[i] == string[i + 2]:
                repeatLetter = True
    if doublePair and repeatLetter:
        niceStrings += 1
print("Nice strings: " + str(niceStrings))