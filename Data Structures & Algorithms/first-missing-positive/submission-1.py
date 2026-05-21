class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # brainstorm with sort
        nums.append(0)
        nums.sort()
        
        missing = nums[-1] + 1
        for i in range(1, len(nums)):
            if nums[i] <= 0:
                continue

            diff = nums[i] - nums[i - 1] if nums[i - 1] > 0 else nums[i] + nums[i - 1]
            if diff > 1:
                return nums[i - 1] + 1

        return missing