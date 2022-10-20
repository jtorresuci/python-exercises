def scramble(s) -> str:
    # 1 Split lists
    list_s = s.split()

    # 2 Run loop and scramble if word has more than 3 characters
    output = ""
    for word in list_s:
        if len(word) > 3:
            pivot = len(word) -2
            scrambled_word = word[:1] + word[pivot] + word[2:pivot] + word[1] + word[pivot+1:]
            output += scrambled_word + " "
        else:
            output += word + " "
    return output
    



def main():
    # 1 Initialize with prompt
    prompt = "Enter a string (blank to quit): "
    s = input(prompt)

    # 2 Enter loop until user enters empty string
    while s != "":
        # 3 Scramble and output words
        print("The scrambled version: " + scramble(s))

        # 4 Prompt user to continue or quit
        s = input(prompt)


        

main()