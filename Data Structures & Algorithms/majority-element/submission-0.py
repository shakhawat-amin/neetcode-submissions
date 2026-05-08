class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        max_value = 0
        target_max = int(len(nums)/2 + 1)
        for num in nums:
            val = dict.get(num, 0) + 1
            max_value = max(val, max_value)
            if max_value == target_max:
                return num
            
            dict[num] = val
        
        return 0
