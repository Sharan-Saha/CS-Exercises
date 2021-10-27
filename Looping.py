def converge(number):
    while number > 1: 
        if number % 2 == 0: 
            number = int(number / 2)
            print(number)
        else: 
            number = int(number * 3) + 1
            print(number)


converge(19)


