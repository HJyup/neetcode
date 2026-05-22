class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = { 0: 1 }
        ans = 0

        # curr - smth = k
        # - smth = k - curr
        # smth = -k + curr
        # smth = curr - k
        curr = 0
        for num in nums:
            curr += num
            ans += seen.get(curr - k, 0)

            seen[curr] = seen.get(curr, 0) + 1 


        return ans
