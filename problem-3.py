import math
def euler3(n):
    r = []
    for i in range(2, int(n**0.5) + 1):
        if math.prod(r) == n:
            return r[-1]
        if (n / i).is_integer():
            for j in range(2, i+1):
                if i % j == 0:
                    break
        else:
            continue
        r.append(i)

print(euler3(600851475143))
