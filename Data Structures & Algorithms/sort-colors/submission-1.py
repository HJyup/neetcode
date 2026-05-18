import random

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partition(left: int, pivot: int) -> int:
            if left >= pivot:
                return left

            random_idx = random.randint(left, pivot)
            nums[random_idx], nums[pivot] = nums[pivot], nums[random_idx]

            right = pivot - 1
            while left <= right:
                if nums[left] >= nums[pivot]:
                    nums[right], nums[left] = nums[left], nums[right]
                    right -= 1
                else:
                    left += 1

            nums[pivot], nums[left] = nums[left], nums[pivot]
            return left
        
        def quick(left: int, right: int) -> None:
            if left >= right:
                return None

            idx = partition(left, right)
            quick(left, idx - 1)
            quick(idx + 1, right)

            return None

        quick(0, len(nums) - 1)
        return nums