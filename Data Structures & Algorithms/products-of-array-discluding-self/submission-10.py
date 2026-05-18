class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1 for _ in range(n)]

        prefix, suffix = 1, 1
        for i in range(n):
            ans[i] *= prefix
            prefix *= nums[i]

            ans[n - i - 1] *= suffix
            suffix *= nums[n - i - 1]

        return ans
        