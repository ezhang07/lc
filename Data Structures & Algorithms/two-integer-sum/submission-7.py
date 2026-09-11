class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {} # value : index

        for i, n in enumerate(nums):
            difference = target - n

            if difference in seen_map:
                return [seen_map[difference], i]
            else:
                seen_map[n] = i
            
        return None