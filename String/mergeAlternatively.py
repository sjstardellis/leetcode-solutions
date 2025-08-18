class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # get the minimum that we can go back and forth with the two words
        minimum = min(len(word1), len(word2))
        res = ""
        # add characters alternatively
        for i in range(minimum):
            res = res + word1[i]
            res = res + word2[i]
        if len(word1) < len(word2):
            # slice the rest fo the characters
            res = res + word2[minimum:]
        if len(word1) > len(word2):
            # slice the rest fo the characters
            res = res + word1[minimum:]
        else:
            # if they are equal, just return
            return res
        return res