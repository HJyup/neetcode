class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0

        buckets = [0] * len(fruits)
        occupied = 0

        l, r = 0, 0
        for r in range(len(fruits)):
            while occupied == 2 and buckets[fruits[r]] == 0:
                buckets[fruits[l]] -= 1
                occupied -= 1 if buckets[fruits[l]] == 0 else 0
                l += 1

            buckets[fruits[r]] += 1
            occupied += 1 if buckets[fruits[r]] == 1 else 0
            
            ans = max(ans, r - l + 1)

        return ans
        