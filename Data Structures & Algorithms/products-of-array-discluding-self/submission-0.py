class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        zero_counter = 0
        result = []
        product = 1
        
        #product skipping 0's
        for num in nums:
            if num == 0:
                zero_counter += 1
                continue
            product *= num

        if zero_counter == 0:
            for num in nums:
                final = int(product / num)
                result.append(final)
        
        elif zero_counter == 1:
            for num in nums:
                if num == 0:
                    result.append(product)
                else:
                    result.append(0)

        else:
            for num in nums: 
                result.append(0)
        
        return result




