def euler5():
    divs = tuple(range(1, 20+1))
    num = 240
    while True:
        if all([num % i == 0 for i in divs]):
            return num
        else:
            num += 240


euler5()
