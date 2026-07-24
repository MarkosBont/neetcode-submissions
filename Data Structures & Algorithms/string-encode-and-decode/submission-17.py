class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for s in strs:
            length = len(s)
            output += str(length) + "." + s
        
        return output


    def decode(self, s: str) -> List[str]:
        left = 0
        right = 1
        output = []

        while right < len(s):
            if s[right] == '.':
                length = int(s[left:right])
                output.append(s[right+1:right+1+length])
                left = right + 1 + length
                right = left + 1
            
            else:
                right += 1
        
        return output



