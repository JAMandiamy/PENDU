
class Guesser:
    _tryed_letters = []
    _found_letters = []
    _word = None

    def __init__(self, word):
        self._word = word

    def found_letters(self):
        return self._found_letters

    def is_guessed(self) -> bool:
        return len(self._word) == len(self._found_letters)

    def in_word(self, new_letter) -> bool:
        return new_letter in self._word

    def mark_letter_as_tryied(self, new_letter):
        self._tryed_letters.append(new_letter)

    def mark_letter_as_found(self, new_letter):
        self._found_letters.append(new_letter)
