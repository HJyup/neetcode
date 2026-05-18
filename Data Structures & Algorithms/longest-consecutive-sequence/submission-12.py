class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        mx = 0

        for num in nums:
            if num - 1 in st:
                continue

            curr, val = 1, num
            while val + 1 in st:
                val += 1
                curr += 1

            mx = max(curr, mx)

        return mx