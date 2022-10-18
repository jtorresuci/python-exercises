def main():
    s = input("Enter a string: ")
    if isPalindrome(s):
        print("That's a palindrome.")
    else:
        print("That isn't a palindrome.")


def isPalindrome(s) -> bool:
    # 1 check if reversed string equals original string
    return s[::-1] == s