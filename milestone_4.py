import random

word_list = ["apple", "banana", "orange", "passionfruit", "guava"]

class Hangman:
    def __init__ (self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letter in self.word:
                if guess == letter:
                    letter_idx = self.word.index(letter)
                    self.word_list[letter_idx] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word")
            print("You have {num_lives} lives left}")

    def ask_for_input(self):
        while True:
            guess = input("Enter a single letter ")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

hangman_1 = Hangman(word_list)
hangman_1.ask_for_input()