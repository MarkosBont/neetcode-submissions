class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            length = len(s)
            output += str(length) + '.' + s
        
        return output


    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        start = 0
        length = 0

        while i < len(s):
            if s[i] == '.':
                length = int(s[start:i])
                string = s[i+1:i+1+length]
                output.append(string)
                i += length + 1
                start = i

            else:
                i += 1
        
        return output

            


