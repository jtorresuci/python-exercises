def findAverage(input_file) -> list:
    infile = open(input_file, "r")

    sum1, sum2, average1, average2, count = 0, 0, 0, 0, 0

    for line in infile:
        count += 1
        numbers = line.split()
        sum1 += float(numbers[0])
        sum2 += float(numbers[1])
    average1 = sum1 / count
    average2 = sum2 / count

    return [average1, average2]

def main():
    infile = input("Enter the input file name: ")
    avg_list = findAverage(infile)
    print("The averages are", avg_list[0], "and", avg_list[1], end ="")
    print(".")

main()
