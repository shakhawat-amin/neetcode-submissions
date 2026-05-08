class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums):
            diff = target-n
            if dic.get(diff, -1) >= 0 :
                return [dic.get(diff), i]
            else:
                dic[n] = i