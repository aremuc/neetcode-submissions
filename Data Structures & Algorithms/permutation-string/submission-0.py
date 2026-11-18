class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False
        
        s1_count = {}
        s2_count = {}
        start = 0
        end = len(s1) - 1

        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1

        for char in range(len(s1)):
            s2_count[s2[char]] = s2_count.get(s2[char], 0) + 1
        
        if s1_count == s2_count:
            return True

        while end < len(s2) - 1:
            if s1_count == s2_count:
                return True
            
            else:
                s2_count[s2[start]] = s2_count.get(s2[start], 0) - 1
                

                if s2_count[s2[start]] <= 0:
                    del s2_count[s2[start]]
                
                start += 1
                end += 1

                s2_count[s2[end]] = s2_count.get(s2[end], 0) + 1
                
                if s1_count == s2_count:
                    return True
        
        return False

        
        