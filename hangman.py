#Global variables will allow the teaching of scope. This program can be rewritten as a class
lives = 3
#Currently takes one-line input as a word. Possible alternatives:
#1. split file by line and use random.choice() (requires split() and random())
f = open("word.txt")
# lower can be left out if not taught, but rstrip must be taught
word = f.read().rstrip().lower()
remaining = len(word) # remaining number of words. Used to check if game is won
display = []
used = [] # Words we have used
for i in range(len(word)):
    display.append("_")

def show_state():
    global lives, used, display
    print("Lives:", lives)
    print("Letters guessed:", "".join(used))
    print("Word so far:", "".join(display))

def turn():
    show_state()
    global word, remaining, display, used, lives
    guess = input("Enter a letter: ")[0].lower()
    if (guess in word):
        print("Correct")
        for i in range(len(word)):
            if word[i] == guess:
               remaining = remaining - 1
               display[i] = guess
    else:
        print("Incorrect")
        #update letters guessed
        if guess not in used:
            used.append(guess)
            lives = lives - 1

def game():
    playing = True
    while playing:
        if lives == 0:
            print("Game over!")
            playing = False;
        elif remaining == 0:
            print("You win!")
            playing = False;
        else:
            turn()

game()



