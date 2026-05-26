class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0

        mn = float('inf')
        for price in prices:
            mn = min(price, mn)
            ans = max(ans, price - mn)

        return ans