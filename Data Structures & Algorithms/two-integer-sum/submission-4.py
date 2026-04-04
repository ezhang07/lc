class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]

        valTable = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in valTable:
                return [valTable[diff],i]
            valTable[n] = i


        
