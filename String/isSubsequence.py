class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # our two pointers
        s1 = 0
        t1 = 0
        # while one of the lengths of the string hasn't been reached
        while t1 < len(t) and s1 < len(s):
            # if we find a match between characters, move both pointers forward
            if s[s1] == t[t1]:
                s1 += 1
            # otherwise just move t pointer forward
            t1 += 1
        # return true if s1 pointer reaches the same size as the length of s (meaning all the characters existed)
        return s1 == len(s)
