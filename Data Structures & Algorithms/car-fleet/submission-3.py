class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position, speed), reverse=True)

        for car in cars:
            arrival = (target - car[0]) / car[1]

            if not stack or arrival > stack [-1]:
                stack.append(arrival)
        
        return len(stack)
        