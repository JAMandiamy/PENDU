#!/bin/python
# -*- coding: utf-8

from word_provider import provide_word
from guessing import Guesser
from formatter import format_word

def run():
    word = provide_word()
    g = Guesser(word)

    while (g.is_guessed() == False):
        new_letter = input("Quelle lettre essayer ?")
        g.mark_letter_as_tryied(new_letter)

        if g.in_word(new_letter):
            g.mark_letter_as_found(new_letter)
            print("Hourra ! Vous avez trouvé une lettre")
            print("Voici le mot à trouver : {}".format(format_word(word, g.found_letters())))

    print("Bravo, le mot a été trouvé")


if __name__ == '__main__':
    run()
