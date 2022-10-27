def repeatedString(s, n):
    size = len(s)
    q = n // size
    r = n % size
    partial_s = s[:r]

    a_count = q * s.count('a') + partial_s.count('a')
    return a_count


def main():
    s = input("String to consider: ")
    n = int(input("Length(n): "))

    count_a = repeatedString(s, n)

    print(count_a)


main()
