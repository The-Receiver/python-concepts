# tries = 0
x = 49;
found = False
while not found:
    # tries = tries + 1
    guess = input("Guess the number between 1 and 100") 
    if guess == x:
        found = True
    else:
        print("Wrong. Guess again")



