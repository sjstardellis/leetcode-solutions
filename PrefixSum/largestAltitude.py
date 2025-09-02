from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain = [0] + gain
        current_sum = 0
        largest_altitude = 0
        for i in range(len(gain)):
            current_sum += gain[i]
            if current_sum > largest_altitude:
                largest_altitude = current_sum

        return largest_altitude