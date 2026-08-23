class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenMap = {} # value: index

        for i, n in enumerate(nums):
            diff = target - n

            if diff in seenMap:
                # return the indices of two numbers
                return [i, seenMap[diff]]
            
            seenMap[n] = i
        
        