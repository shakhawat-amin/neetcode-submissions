class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in nums:
            if dict.get(i, None) != None:
                return True
            else:
                dict[i] = i
        
        return False

        