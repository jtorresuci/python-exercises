def divisibleSumPairs(n, k, ar):
    size = len(ar)
    count = 0
    for i in range(size):
        for j in range(i+1, size):
            sum = ar[i] + ar[j]
            if sum >= k and sum % k == 0:
                count += 1
    return count