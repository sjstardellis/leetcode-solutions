# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left_bound = 1
        right_bound = n
        # while the bounds haven't crossed yet
        while left_bound <= right_bound:
            # calculate the middle
            mid = (left_bound + right_bound) // 2
            # get the result from api
            result = guess(mid)
            # found number case
            if result == 0:
                return mid
            # num > pick, shift right bound
            elif result == -1:
                right_bound = mid - 1
            # num < pick, shift left bound
            else:
                left_bound = mid + 1
