class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''

        for s in strs:
            length = len(s)
            encoded_string += str(length) + '.'
            encoded_string += s
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []

        while i < len(s):
            j = i
            while s[j] != '.':
                j += 1
            
            length = int(s[i:j])
            string = s[j+1:j+length+1]
            print(string)
            output.append(string)
            i = j+length+1
        
        return output



            
        
