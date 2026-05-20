class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for st in strs:
            length = len(st)
            encoded.append('[' + str(length) + ']' + st)

        print(encoded)
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        def getDigit(i: int) -> (int, int):
            digit = 0

            while i < len(s) and s[i] != ']':
                digit = digit * 10 + int(s[i])
                i += 1

            return (digit, i + 1)

        decoded = []

        # [5]Hello[5]World

        i = 0
        while i < len(s):
            length, upd = getDigit(i + 1)
            i = upd

            st = []
            for j in range(length):
                st.append(s[i + j])

            decoded.append(''.join(st))    
            i += length

        return decoded