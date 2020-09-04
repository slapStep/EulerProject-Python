def isPalindrom(v):
    return str(v) == str(v)[::-1]


def euler4(n):
    palindroms = []
    start = int('9' + '0' * (n-1))
    end = int('9' + '9' * (n-1))

    for num in range(start, end+1):
        for i in range(num, end+1):
            if isPalindrom(num * i):
                palindroms.append(num * i)
    return max(palindroms)


print(euler4(3))
