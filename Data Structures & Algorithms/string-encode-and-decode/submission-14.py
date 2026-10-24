class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for string in strs:
            output += str(len(string)) + '.' + string

        return output

    def decode(self, s: str) -> List[str]:

        left = 0
        right = 1

        output = []

        while right < len(s):
            if s[right] == '.':
                length = int(s[left:right])
                if length == 0:
                    return [""]
                string = s[right+1:right+1+length]
                output.append(string)

                left = right + 1 + length
                right += length
            
            else:
                right += 1
        

        return output
            

