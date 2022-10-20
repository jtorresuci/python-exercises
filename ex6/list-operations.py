list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [4, 6, 8, 6, 12]
list_3 = [5, 10, 15, 200, 25, 50, 20]

list_4 = ["M", "na", "i", "Ke"]
list_5 = ["y", "me", "s", "lly"]

# 1 reverse list_1
print(list_1[::-1])

# 2 remove all occurences of 6
while 6 in list_2:
    list_2.remove(6)
print(list_2)

# 3 find 20 and remove it
list_3.remove(20)
print(list_3)

# 4 
output = []
for i in range(len(list_4)):
    output.append(list_4[i] + list_5[i])

print(output)