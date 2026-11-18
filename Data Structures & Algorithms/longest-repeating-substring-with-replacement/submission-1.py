class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        if len(s) <= 1:
            return len(s)

        hashmap = {}

        start = 0
        end = 1
        result = 0

        hashmap[s[start]] = hashmap.get(s[start], 0) + 1

        while end < len(s):

            hashmap[s[end]] = hashmap.get(s[end], 0) + 1

            while ((end - start + 1) - max(hashmap.values())) > k:
                hashmap[s[start]] -= 1
                start += 1

            result = max(result, end - start + 1)
            
            end += 1

        return result