class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # empty needle
        if not needle:
            return 0

        # default to -1, unless a match is found
        index = -1
        # you only need to check starting positions
        # where there’s still enough characters left in haystack to possibly fit needle
        for i in range(len(haystack) - len(needle) + 1):
            # compare first char of needle to the current index of haystack
            if haystack[i] == needle[0]:
                # mark the start of the index
                index = i
                # go through the needle string
                for j in range(len(needle)):
                    # if there is a mismatch, break the checking loop and reset index to -1
                    if haystack[i + j] != needle[j]:
                        index = -1
                        break
                # if there is a match found, return the index
                if index != -1:
                    return index

        return index
