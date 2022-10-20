def main():
    # 1 initialize prompts
    prompt = "Enter your password: "
    prompt2 = "Re-enter your password: "
    invalid = "That password didn't have the required properties."
    valid = "That pair of passwords will work."
    set = False

    # 2 run loop to check if passwords match
    while not set:
        s = input(prompt)
        s2 = input(prompt2)
        if s != s2:
            print("That passwords don't match")
        # 3 check if password meets requirements
        elif isValidPassword(s) == False:
            print(invalid)
        # 4 requirements met
        else:
            set = True
            print(valid)

def isValidPassword(s) -> bool:
    # 1 check if required lenght is met
    if len(s) < 7:
        return False

    upper = False
    lower = False
    digit = False
    symbol = False

    # 2 check each character for lower, upper, digit, and symbol
    for char in s:
        if char == char.lower() and char.isdigit() == False and not(char in "#@&") :
            lower = True
        if char == char.upper() and char.isdigit() == False and not(char in "#@&"):
            upper = True
        if char in "1234567890":
            digit = True
        if char in "#@&":
            symbol = True
    
    # 3 if all conditions are met return true
    return (upper and lower and digit and symbol)
    
main()