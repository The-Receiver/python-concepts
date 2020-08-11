class hangman:
    def __init__(self):
        self.lives = 3
        self.f= open("word.txt")
        self.word = self.f.read().rstrip().lower()
        self.remaining = len(self.word) # remaining number of words. Used to check if game is won
        self.display = []
        self.used = [] # Words we have used
        for i in range(len(self.word)):
            self.display.append("_")

    def show_state(self):
        print("Lives:", self.lives)
        print("Letters guessed:", "".join(self.used))
        print("Word so far:", "".join(self.display))

    def turn(self):
        self.show_state()
        self.guess = input("Enter a letter: ")[0].lower()
        if (self.guess in self.word):
            print("Correct")
            for i in range(len(self.word)):
                if self.word[i] == self.guess:
                   self.remaining = self.remaining - 1
                   self.display[i] = self.guess
        else:
            print("Incorrect")
            #update letters guessed
            if self.guess not in self.used:
                self.used.append(self.guess)
                self.lives = self.lives - 1

    def game(self):
        self.playing = True
        while self.playing:
            if self.lives == 0:
                print("Game over!")
                self.playing = False;
            elif self.remaining == 0:
                print("You win!")
                self.playing = False;
            else:
                self.turn()

h = hangman()
h.game()



