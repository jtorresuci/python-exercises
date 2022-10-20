def is_prime(n) -> bool:
    check_n = 1

    for i in range(2, n):
        check_n = n % i
        if check_n == 0:
            break

    if check_n != 0:
        return True
    else:
        return False

def main():
    prime_lists = []
    for i in range(2, 101):
        prime_lists.append(i)
    
    # print(prime_lists)

    
    for num in prime_lists:
        if not is_prime(num):
            print(num)
            prime_lists.remove(num)
    print(prime_lists)


main()

print(is_prime(9))