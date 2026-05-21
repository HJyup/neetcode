class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # the key idea:
        # if we have let's say 4 numbers (n), then our solution must be from [1, 4].
        # so we need to have some sort of padding.
        
        # the first value that has to be
        i = 0

        while i < len(nums):
            while nums[i] <= len(nums) and nums[i] > 0 and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

            i += 1

        # find ans
        for i in range(len(nums)):
            if i != nums[i] - 1:
                return i + 1

        return len(nums) + 1