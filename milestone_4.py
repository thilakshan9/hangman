import random

class Hangman:
    def __init__ (word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = [''] * len(self.word)
        self.num_letters = len(set(word))
        self.num_lives = num_lives
        self.word_list = word_list
        list_of_guesses = []
