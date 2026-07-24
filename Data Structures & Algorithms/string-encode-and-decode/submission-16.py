class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for string in strs:
            output += str(len(string)) + '.' + string

        return output

    def decode(self, s: str) -> List[str]:
        if len(s) == 2:
            return [""]

        left = 0
        right = 1

        output = []

        while right < len(s):
            if s[right] == '.':
                length = int(s[left:right])
                string = s[right+1:right+1+length]
                output.append(string)

                left = right + 1 + length
                right = left + 1
            
            else:
                right += 1
        

        return output
            

