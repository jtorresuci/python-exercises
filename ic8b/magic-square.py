def main():
    table = [
    [16, 3, 2, 13],
    [5, 10, 11, 8], 
    [9, 6, 7, 12], 
    [4, 15, 14, 1]
    ]
    
    # table = [
    # [16, 3, 2, 13],
    # [5, 10, 11, 9], 
    # [9, 6, 7, 12], 
    # [4, 15, 14, 1]
    # ]

    if magic_square(table):
        print("It is a magic square")
    else:
        print("It is not a magic square")

def magic_square(table):
    row_sum_list = []
    row_sum = 0
    column_sum_list = [0, 0, 0, 0]
    column_sum = 0
    diagonal_sum = 0

    for i in range(len(table)):
        for j in range(len(table[i])):
            print(table[i][j], end = "  ")
            row_sum += table[i][j]
            column_sum_list[i] += table[i][j]
            
        row_sum_list.append(row_sum)
        row_sum = 0
        diagonal_sum += table[i][i]

        print("")
    
    if row_sum_list == column_sum_list and row_sum_list[0] == diagonal_sum:
        return True
    else:
        return False

main()