prompt = "Enter values (blank line to quit): "
nums = []

while True:
    s = input(prompt)
    if s == "" and (not s.isdigit()):
        break
    else:
        # print(s)
        nums.append(int(s))

output = 0
for i in range(len(nums)):
    if i % 2 != 0:
        output -= nums[i]
    else:
        output += nums[i]

print(output)