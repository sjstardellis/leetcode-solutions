from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if the list is empty, return ""
        if not strs:
            return ""

        # start with the prefix being the first word
        prefix = strs[0]

        # compare prefix with each word, index 1 instead of 0
        for word in strs[1:]:
            # shorten prefix until it matches the start of the word
            while not word.startswith(prefix):
                # take everything from the start to (but not including) the last character
                prefix = prefix[:-1]
                # if empty
                if not prefix:
                    return ""

        return prefix
