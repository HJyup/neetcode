from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        check, window = defaultdict(int), defaultdict(int) # can be done via arr though
        min_l, idx = float('inf'), -1

        for ch in t:
            check[ch] += 1

        l, needed = 0, len(check.keys())
        for r in range(len(s)):
            window[s[r]] += 1
            needed -= 1 if window[s[r]] == check[s[r]] else 0 # we want to cross it only once
            while needed == 0:
                dst = r - l + 1
                if dst < min_l:
                    min_l = dst
                    idx = l
                needed += 1 if window[s[l]] == check[s[l]] and window[s[l]] != 0 else 0
                window[s[l]] -= 1
                l += 1

        return s[idx: idx + min_l] if min_l != float('inf') else ""