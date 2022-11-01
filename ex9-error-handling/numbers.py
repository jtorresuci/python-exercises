def main():
    num = -1
    nums = []
    flag_1 = False
    flag_2 = False
    while not flag_2:
        # Check for first non-digit
        if flag_1 == False:
            try:
                num = int(input("Enter a number, or 2 non-numbers to quit: "))
                nums.append(num)
            except ValueError:
                flag_1 = True
                continue
        # Check for second non-digit 
        if flag_1 == True:
            try:
                num = int(input("Enter a number, or another non-number to quit: "))
                nums.append(num)
                flag_1 = False
            except ValueError:
                flag_2 = True
                continue
    print("The total is ", sum(nums))

main()