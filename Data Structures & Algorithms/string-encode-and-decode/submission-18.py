class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            length = len(s)
            output += str(length) + '.' + s
        
        print(output)
        return output


    def decode(self, s: str) -> List[str]:
        if len(s) == 2:
            return [""]
        output = []
        i = 0
        start = 0
        while i < len(s):
            length = 0
            if s[i] == '.':
                length = int(s[start:i])
                string = s[i+1:i+1+length]
                output.append(string)
                i += length
                start = i+1

            else:
                i += 1
        
        return output

            


