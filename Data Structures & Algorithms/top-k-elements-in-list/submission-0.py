class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        frequent_vals = []

        for num in nums:
            count[num] = count.get(num, 0) + 1

        sorted_count = sorted(count, key=count.get, reverse=True)

        for value in range(k):
            frequent_vals.append(sorted_count[value])
        
        return frequent_vals

