class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''

        for s in strs:
            length = len(s)
            encoded_string += str(length) + '.'
            encoded_string += s
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        start_index = 0
        output = []

        for i, char in enumerate(s):
            if char == '.':
                start_index = i-1
                length = int(s[start_index:i])
                string = s[i+1:i+length+1]
                output.append(string)
                

        return output



            
        
