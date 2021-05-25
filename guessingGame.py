import random
n = random.randint(1,9)
ch = 0
while ch<5:
    guess = int(input("Enter a number from 1 to 9"))
    ch = ch + 1
    if n == guess:
        print("Congratulations, you won.")
        break
    elif guess < n:
        print("Try again, you guessed too low.")
    else:
        print("Try again, you guessed too high.")
if not ch < 5:
    print("You lost, the number is", n)
