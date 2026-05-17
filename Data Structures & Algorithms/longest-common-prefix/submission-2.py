class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []

        i = 0
        while i < len(strs[0]):
            if i >= len(strs[0]):
                return ''.join(res)
            
            for word in strs[1:]:
                if i >= len(word) or word[i] != strs[0][i]:
                    return ''.join(res)

            res.append(strs[0][i])          
            i += 1

        return ''.join(res)