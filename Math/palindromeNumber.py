class Solution:
    def isPalindrome(self, x: int) -> bool:
        # convert int to string to iterate
        x = str(x)

        pointer1 = 0
        pointer2 = len(x) - 1

        # move each pointer, if they don't match each move then return false
        while pointer1 < pointer2:
            if x[pointer1] != x[pointer2]:
                return False
            pointer1 += 1
            pointer2 -= 1
        return True