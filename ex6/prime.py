def is_prime(n) -> bool:
    check_n = 1
    prime = True

    for i in range(2, n):
        if(i == n):
            continue
        else:
            check_n = n % i
        
        if check_n == 0:
            # print("Break")
            prime = False
            # print(check_n)
            break
    return prime

def main():
    prime_lists = []
    for i in range(2, 101):
        prime_lists.append(i)
    
    # print(prime_lists)

    
    for num in prime_lists:
        prime = is_prime(num)
        print(num)
        print(prime)
        if prime == False:
            # print(num)
            prime_lists.remove(num)
    print(prime_lists)


main()

# print(is_prime(100))