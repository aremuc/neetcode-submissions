class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        seen = set(nums)

        if len(nums) == 1:
            return 1
            
        for num in seen:
            if (num - 1) in seen:
                continue
            
            current = num
            length = 1

            while (current + 1) in seen:
                current += 1
                length += 1

            result = max(result, length)

        return result



        