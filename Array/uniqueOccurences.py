from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = {}
        # log all the frequencies of the array
        for i in range(len(arr)):
            seen[arr[i]] = seen.get(arr[i], 0) + 1
        # create a set
        unique = set()

        # if the value (of the seen hashmap) has already been put in the new hashset, return false
        for val in seen.values():
            if val in unique:
                return False
            # otherwise add the value to the hash set
            unique.add(val)
        return True
