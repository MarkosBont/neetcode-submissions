class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""

        for s in strs:
            length = str(len(s))
            encoding += length + '.' + s

        return encoding


    def decode(self, s: str) -> List[str]:
        i = 0
        output = []

        while i < len(s):
            j = i 
            while s[j] != '.':
                j += 1
            
            length = int(s[i:j])
            string = s[j+1:j+1+length]
            output.append(string)

            i = j + 1 + length

        return output

