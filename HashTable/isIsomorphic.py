class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # two hash maps
        hash1 = {}
        hash2 = {}

        # iterate over characters of both strings in parallel
        for ch1, ch2 in zip(s, t):
            # if ch1 was already mapped before, it must map to the same ch2
            if ch1 in hash1 and hash1[ch1] != ch2:
                return False
                        # if ch2 was already mapped before, it must map to the same ch1
            if ch2 in hash2 and hash2[ch2] != ch1:
                return False
            # establish the mapping between ch1 <-> ch2
            hash1[ch1] = ch2
            hash2[ch2] = ch1
        # if no issues were found, the strings are isomorphic
        return True
