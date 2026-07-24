class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ''
        for s in strs:
            length = len(s)
            final += str(length) + '.'
            final += s
        
        return final

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != ".":
                j += 1
            
            length = int(s[i:j])
            string = s[j+1:j+length+1]
            output.append(string)
            i  = j + length + 1
        
        return output



