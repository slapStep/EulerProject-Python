def euler6():
    sumOfSquares = sum([x ** 2 for x in range(1, 100 + 1)])
    squareOfSum = sum(range(100 + 1)) ** 2
    return squareOfSum - sumOfSquares


print(euler6())  # result 25164150
