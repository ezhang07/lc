class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diffTable = {}

        for i, n in enumerate(nums):
            diff = target - n

            if n in diffTable:
                return [diffTable[n], i]

            diffTable[diff] = i