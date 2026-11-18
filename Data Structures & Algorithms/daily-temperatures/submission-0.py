class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            current_temp = temperatures[i]

            while stack and current_temp > temperatures[stack[-1]]:
                previous_index = stack.pop()
                result[previous_index] = i - previous_index

            stack.append(i)

        return result
