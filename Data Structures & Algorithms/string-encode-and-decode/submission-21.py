class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ''

        for s in strs:
            length = str(len(s))
            final += length + '.' + s
        
        print(final)
        return final

    def decode(self, s: str) -> List[str]:
        strs = []

        p1 = 0
        p2 = 0

        while p2 < len(s):
            while s[p2] != '.':
                p2 += 1
            
            length = int(s[p1:p2])
            word = s[p2+1:p2+length+1]
            strs.append(word)

            p2 = p2 + length + 1
            p1 = p2

        return strs


