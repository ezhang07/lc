class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # make a hashmap with target - nums[i] : i
        mp = {} # target - nums[i] : i

        for i, n in enumerate(nums):
            if n in mp:
                return [mp[n], i]
            diff = target - n
            mp[diff] = i
