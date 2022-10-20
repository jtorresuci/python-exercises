def sameElements(l1, l2):
    return sorted(l1) == sorted(l2)

def main():
    # l1 = [1, 3, 1, 1, 2]
    # l2 = [1, 1, 1, 2, 3]

    # l1 = [1, 3, 1, 1, 2]
    # l2 = [1, 1, 1, 2, 1]

    l1 = [1, 1, 1, 1, 2]
    l2 = [1, 1, 1, 2]
    print("List 1 is ", l1)
    print("List 2 is ", l2)
    print("The lists contains the same elements:", sameElements(l1, l2))

main()