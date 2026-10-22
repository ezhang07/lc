class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in seenMap:
                return [seenMap[diff], i]
            seenMap[n] = i
        
        return -1