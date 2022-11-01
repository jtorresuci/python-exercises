def main():
    infile = open("input.txt", "r")
    lines = []
    for line in infile:
        lines.append(line.rstrip())

    lines.reverse()

    for line in lines:
        print(line, "\n")
    
main()