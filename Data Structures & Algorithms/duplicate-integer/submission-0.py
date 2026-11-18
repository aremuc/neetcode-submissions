class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
                continue
            if i in seen:
                return True
        return False
        