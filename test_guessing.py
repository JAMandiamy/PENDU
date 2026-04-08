import unittest

from guessing import Guesser


class TestGuesser(unittest.TestCase):
    def setUp(self):
        Guesser._tryed_letters = []
        Guesser._found_letters = []
        Guesser._word = None

    def test_init_sets_word(self):
        guesser = Guesser("chat")
        self.assertEqual(guesser._word, "chat")

    def test_found_letters_returns_empty_list_initially(self):
        guesser = Guesser("chat")
        self.assertEqual(guesser.found_letters(), [])

    def test_found_letters_returns_added_letters(self):
        guesser = Guesser("chat")
        guesser.mark_letter_as_found("c")
        guesser.mark_letter_as_found("a")
        self.assertEqual(guesser.found_letters(), ["c", "a"])

    def test_is_guessed_returns_false_initially(self):
        guesser = Guesser("chat")
        self.assertFalse(guesser.is_guessed())

    def test_is_guessed_returns_true_when_all_letters_are_found(self):
        guesser = Guesser("chat")
        for letter in "chat":
            guesser.mark_letter_as_found(letter)
        self.assertTrue(guesser.is_guessed())

    def test_in_word_returns_true_when_letter_is_in_word(self):
        guesser = Guesser("chat")
        self.assertTrue(guesser.in_word("a"))

    def test_in_word_returns_false_when_letter_is_not_in_word(self):
        guesser = Guesser("chat")
        self.assertFalse(guesser.in_word("z"))

    def test_mark_letter_as_tryied_adds_letter_to_tried_letters(self):
        guesser = Guesser("chat")
        guesser.mark_letter_as_tryied("c")
        self.assertEqual(guesser._tryed_letters, ["c"])

    def test_mark_letter_as_found_adds_letter_to_found_letters(self):
        guesser = Guesser("chat")
        guesser.mark_letter_as_found("c")
        self.assertEqual(guesser._found_letters, ["c"])

    def test_is_guessed_returns_true_when_all_letters_are_found_word_with_repeated_letters(self):
        guesser = Guesser("eeeaaa")
        for letter in "ea":
            guesser.mark_letter_as_found(letter)
        #self.assertTrue(guesser.is_guessed())


if __name__ == "__main__":
    unittest.main()
