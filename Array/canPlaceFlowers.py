from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # add 0 padding, helps with edge cases
        flowerbed = [0] + flowerbed + [0]

        # keep track how many flowers we can place
        can_place = 0

        # loop through the flowerbed, but skip the first and last element (we added those elements)
        for i in range(1, len(flowerbed) - 1):

            # check to see if the current spot and neighbors are empty
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:

                # plant the flower at the current position
                flowerbed[i] = 1

                # increment count
                can_place += 1

        # if we can place at least n or greater flowers, return true
        return can_place >= n
