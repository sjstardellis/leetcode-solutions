class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash1 = {}
        hash2 = {}

        for ch in ransomNote:
            hash1[ch] = hash1.get(ch, 0) + 1
        for ch in magazine:
            hash2[ch] = hash2.get(ch, 0) + 1
        # go through all the characters in hash1 (ransom hash)
        for ch in hash1:
            # if the character count for the current key-value entry is greater than the current character in hash2
            # if not, default to 0
            if hash1[ch] > hash2.get(ch, 0):
                return False
        return True
