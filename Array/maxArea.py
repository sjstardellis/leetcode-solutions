from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # keep track of our maximum area
        max_area = 0
        # our two pointers
        left = 0
        right = len(height) - 1

        # keep calculating until pointers intersect
        while left < right:
            # calculate the area
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            # move the smallest pointer inward
            # the left line is shorter, so no matter what, the water level is limited by it
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area