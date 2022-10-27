def swap_first_last(list1):
    last_idx = len(list1) - 1

    temp = list1[0]
    list1[0] = list1[last_idx]
    list1[last_idx] = temp


# def shift_right(list1):
#     list1 = [list1[len(list1) -1]] + list1[1:len(list1) - 1] + list1[:1]
#     return list1


def shift_right(list1):
    e1 = list1[-1]
    print(e1)
    for i, e2 in enumerate(list1):
        list1[i], e1 = e1, e2
    return list1


def replace_even(list1):
    for i in range(len(list1)):
        if list1[i] % 2 == 0:
            list1[i] = 0


def replace_neighbors(list1):
    for i in range(1, len(list1) - 1):
        if list1[i] < list1[i + 1]:
            list1[i] = list1[i + 1]


def remove_middle(list1):
    size = len(list1)
    if size % 2 == 0:
        list1.remove(list1[size//2])
        list1.remove(list1[size//2 + 1])


def even_to_front(list1):
    move_evens = []
    for num in list1:
        if num % 2 == 0:
            move_evens.append(num)
            list1.remove(num)
    i = len(list1) - 1
    while i != -1:
        list1.insert(0, move_evens[i])
        i -= 1


def second_largest(list1):
    print("second_largest")


def is_increasing(list1):
    print("is_increasing")


def has_adjacent_duplicate(list1):
    print("has_adjacent_duplicate")


def has_duplicate(list1):
    print("has_adjacent_duplicate")


def main():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(shift_right(list1))


main()
