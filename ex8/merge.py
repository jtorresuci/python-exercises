def main():
    a = [1, 4, 9, 16]
    b = [9, 7, 4, 9, 11]

    print("List a is", a)
    print("List b is", b)

    result = merge(a, b)
    print("The merged list is", result)


def merge(a, b) -> list:
    output = []
    i = 0
    j = 0

    while i < len(a) or j < len(b):
        if i < len(a):
            output.append(a[i])
            i += 1
        if j < len(b):
            output.append(b[j])
            j += 1
        
        
    return output

main()