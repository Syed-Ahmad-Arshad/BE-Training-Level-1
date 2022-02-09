def fibonacci_generator(number):
    prev_2 = 1
    prev_1 = 1
    for i in range(1, number + 1):
        if i == 1:
            print(prev_1)
        elif i == 2:
            print(prev_2)
        else:
            num = prev_1 + prev_2
            prev_2 = prev_1
            prev_1 = num
            print(num)


number = input("Enter the number of fibonaccis you want: ")
fibonacci_generator(int(number))
