class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}

        for ch in s:
            s_count[ch] = s_count.get(ch, 0) + 1

        for ch in t:
            t_count[ch] = t_count.get(ch, 0) + 1

        return s_count == t_count