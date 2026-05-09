class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = []
        if nums.count(0) >= 2:
            return [0] * len(nums)
        
        for num in nums:
            if num != 0:
                product *= num
        
        if nums.count(0) == 1:
            for num in nums:
                if num == 0:
                    res.append(product)
                else:
                    res.append(0)
        
        else:
            for num in nums:
                res.append(product//num)


        return res

