def printPrimeNumbers(limit):
    for i in range(1, limit + 1):
        is_divisible = 0
        for j in range(1, i + 1):
            if i % j == 0:
                is_divisible = is_divisible + 1
        if is_divisible == 2:
            print(i)


printPrimeNumbers(100)