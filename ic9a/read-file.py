infile = open("input3.txt", "r")
line = infile.readline()

for line in infile:
    line = line.rsplit()

print(line)