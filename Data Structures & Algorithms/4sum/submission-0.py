class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []

        for a in range(len(nums)):
            if a > 0 and nums[a - 1] == nums[a]:
                continue

            for b in range(a + 1, len(nums)):
                if b > a + 1 and nums[b - 1] == nums[b]:
                    continue

                c, d = b + 1, len(nums) - 1
                while c < d:
                    sm = nums[a] + nums[b] + nums[c] + nums[d]

                    if sm > target:
                        d -= 1

                    elif sm < target:
                        c += 1

                    else:
                        ans.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1

                        while c < d and nums[c - 1] == nums[c]:
                            c += 1

                        while c < d and nums[d + 1] == nums[d]:
                            d -= 1

        return ans
        