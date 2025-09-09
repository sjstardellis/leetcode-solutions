class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # remove all spaces, turn into array
        no_spaces = s.split()
        # return last element
        return len(no_spaces[-1])