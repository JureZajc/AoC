input = "yzbqklnj"

# Part 1
import hashlib
i = 0
while True:
    hash = hashlib.md5((input + str(i)).encode("utf-8")).hexdigest()
    if hash[:5] == "00000":
        print("Part 1: " + str(i))
        break
    i += 1

# Part 2
i = 0
while True:
    hash = hashlib.md5((input + str(i)).encode("utf-8")).hexdigest()
    if hash[:6] == "000000":
        print("Part 2: " + str(i))
        break
    i += 1