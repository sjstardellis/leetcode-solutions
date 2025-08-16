class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # our two dictionaries
        hash1 = {}
        hash2 = {}
        # length check
        if len(s) != len(t):
            return False
        # store our characters in dictionary
        for ch1 in s:
            hash1[ch1] = hash1.get(ch1, 0) + 1
        for ch2 in t:
                hash2[ch2] = hash2.get(ch2, 0) + 1
        # compare dictionaries
        return hash1 == hash2