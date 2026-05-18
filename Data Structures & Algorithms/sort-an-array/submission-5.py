import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # -50,000 <= nums[i] <= 50,000 ->
        DISTINCT_ELEMENTS = 50000

        buckets = [0 for _ in range((DISTINCT_ELEMENTS * 2) + 1)]

        for num in nums:
            buckets[num + DISTINCT_ELEMENTS] += 1

        ans = []
        for i, count in enumerate(buckets):
            for _ in range(count):
                ans.append(i - DISTINCT_ELEMENTS)

        return ans