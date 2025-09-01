class Solution:
    def reverseVowels(self, s: str) -> str:
        # dictionary of vowels
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        # convert string to list of characters
        s = list(s)
        # initialize our pointers, beginning and end
        pointer1, pointer2 = 0, len(s) - 1

        # while they have not crossed yet
        while pointer1 < pointer2:
            # if pointer1 is not a vowel, continue moving pointer forwards
            if s[pointer1] not in vowels:
                pointer1 += 1
                continue
            # if pointer2 is not a vowel, continue moving pointer backwards
            if s[pointer2] not in vowels:
                pointer2 -= 1
                continue
            # if we reach this step, then switch vowels
            s[pointer1], s[pointer2] = s[pointer2], s[pointer1]
            # move pointers
            pointer1 += 1
            pointer2 -= 1

        # convert back to String
        return "".join(s)
