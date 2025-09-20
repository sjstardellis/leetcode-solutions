from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # resultant hash table
        res = {}
        # go through each string in the list of strings
        for s in strs:
            # sort the string and make that the key for the hash table
            key = "".join(sorted(s))
            # if the key is not in the result
            if key not in res:
                # create an empty list with the key
                res[key] = []
            # append the original string to the value
            res[key].append(s)
        # return a list of the values in the hash table
        return list(res.values())