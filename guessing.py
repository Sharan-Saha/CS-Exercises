import random

def guess( num):
    
    guesses=0
    while True:
        my_guess=int(input("Enter your guess: "))

        if my_guess < num:
            print("too low")
            guesses += 1
        elif my_guess > num:
            print("too high")
            guesses += 1
        else: 
            print("correct!")
            break

    print(f"you got this in {guesses} guesses")
            
    

def main():
    number = random.randrange(0, 100)
    #user_guess = int(input("Enter your guess: "))
    
    guess( number)


main()