# [0 1 0 0 2 2 1]
# [1 0 1 2 1 0 2 1] 
# [1 0 2 1]
# [0 1 2]


 

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, cand, end = 0, 0, len(nums) -1

        while cand <= end:
            if nums[cand] == 0:
                nums[start], nums[cand] = nums[cand], nums[start]
                start += 1
                cand += 1
            elif nums[cand] == 2:
                nums[end], nums[cand] = nums[cand], nums[end]
                end -= 1
            else:
                cand += 1
                
        

        