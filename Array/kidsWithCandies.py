from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []

        # max candies is the highest number in the array
        max_candies = max(candies)
        for c in candies:
            # if the current candy + the extraCandies is => the maximum number in the regular candies array
            if c + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result
