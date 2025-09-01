import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # create our minheap we're going to use
        min_heap = []

        for num in nums:
            # push current number into heap
            heapq.heappush(min_heap, num)

            # if the heap grows larger than k, remove the smallest element (root of min-heap)
            # this ensures the heap only contains the k largest elements seen so far
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # after processing all numbers, the heap contains the k largest elements
        # the smallest among them (root) is the kth largest overall
        return min_heap[0]