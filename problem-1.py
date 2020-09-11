def euler1(n):
    # return sum([x for x in range(n) if x % 3 == 0 or x % 5 == 0])
    # or
    
    # [3, 6, 9, 12, 15, 18, 21...n] == 3 * [1, 2, 3, 4, 5, 6, 7...n]
    n3 = (n-1) // 3 # multiples of 3 in range(1, n)
    n5 = (n-1) // 5 # multiples of 5 in range(1, n)
    n15 = (n-1) // 15 # multiples of 15 in range(1, n) to remove duplicates of multiples 3 and 5 
    
    # sum of n-numbers: 1 + 2 + 3 + 4 + ... + n equals to = n * (n + 1) / 2
    sum3 = 3 * n3 * (n3 + 1) // 2
    sum5 = 5 * n5 * (n5 + 1) // 2
    sum15 = 15 * n15 * (n15 + 1) // 2
    return sum3 + sum5 - sum15

print(euler1(1000))