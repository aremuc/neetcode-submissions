class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)
        
        characters = {}

        start = 0
        end = 1
        result = 0
        length = 0

        characters[s[start]] = 1

        while end < len(s):

            characters[s[end]] = characters.get(s[end], 0) + 1

            # if duplicate, not counting length yet
            while characters[s[end]] > 1:
                characters[s[start]] -= 1
                start += 1
            
            length = end - start + 1

            result = max(result, length)

            end += 1
        
        return result
            

                 

            
