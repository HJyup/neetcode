import random

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 3-way merge
        n = len(nums)

        # left - represent red
        # mid - represent white
        # right - represent blue

        # place all zeros first
        left, i = 0, 0

        while i < n and left < n:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1

            i += 1

        right = n - 1
        while left <= right:
            if nums[left] == 2:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1

            else:
                left += 1
            
        return nums
