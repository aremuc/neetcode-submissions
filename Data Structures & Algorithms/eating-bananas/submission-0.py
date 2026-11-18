class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        start = 1
        end = max(piles)
        answer = end

        while start <= end:
            mid = (start + end) // 2
            time = 0

            for pile in piles:
                time += pile // mid

                if pile % mid != 0:
                    time += 1

            if time <= h:
                answer = mid
                end = mid - 1

            
            else:
                start = mid + 1
        
        return answer

            