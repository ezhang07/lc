class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        hashmap approach {value : index}

        missingValue = target - nums[i]

        if we can find missingValue in the hashmap
        we have both values needed to sum to target
        and return their indices

        """

        seen_map = {}

        for i, n in enumerate(nums):
            missing_value = target - n
            if missing_value in seen_map:
                return [seen_map[missing_value], i]
        
            seen_map[n] = i
        