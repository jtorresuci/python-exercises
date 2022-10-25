infile = open("input3.txt", "r")
line = infile.readline()


# while line != "":
#     line = infile.readline()
#     print(line)

for line in infile:
    line = line.rsplit()

print(line)