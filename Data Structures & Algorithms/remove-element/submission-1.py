class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        copy = nums.copy()
        for num in copy:
            if num == val:
                nums.remove(val)
   
        return len(nums)
