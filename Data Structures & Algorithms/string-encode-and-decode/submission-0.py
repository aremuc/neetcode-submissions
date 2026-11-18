class Solution:

    def encode(self, strs: List[str]) -> str:

        code = ""

        for word in strs:
            code += str((len(word)))
            code += "#"
            code += word
        
        return code

    def decode(self, s: str) -> List[str]:

        current = 0
        end = 0
        result = []

        while current < len(s):
            end = current

            while s[end] != '#':
                end += 1
            
            length = int(s[current:end])
            word = s[end + 1 : end + 1 + length]
            result.append(word)

            current = end + 1 + length

        return result

        
