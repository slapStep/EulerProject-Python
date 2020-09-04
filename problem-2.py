def euler2(n):
    prev, cur = 1, 1
    s = 0

    for _ in range(1, n+1):
        prev, cur = cur, prev + cur
        if prev % 2 == 0 and prev < 4000000:
            s += prev
        elif prev > 4000000:
            return s
    return s


print(euler2(4000000))
