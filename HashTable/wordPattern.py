class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # split up the string into array of strings, removing spaces
        words = s.split()
        # pattern check
        if len(pattern) != len(words):
            return False
        # maps character to word
        char_to_word = {}
        # maps word to character
        word_to_char = {}

        # go through each word and character
        for character, word in zip(pattern, words):
            # if the character already maps to a word and doesn't match the word its mapped to, return false
            if character in char_to_word and char_to_word[character] != word:
                return False
            # REVERSE
            # if the word already maps to a character and doesn't match the character its mapped to, return false
            if word in word_to_char and word_to_char[word] != character:
                return False
            # if there is no contraction, add the character and word mapping
            char_to_word[character] = word
            word_to_char[word] = character

        return True
