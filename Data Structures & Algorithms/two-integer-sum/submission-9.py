class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        initial approach: nested for loop, add up the indexed values
        if sum == target, return indices

        optimized:
        hashmap -> value : index
        we compute difference = target - indexed value
        if that's inside our hashmap, we know we've seen the other piece of the puzzle
            we would access the key value pair.
        if we don't see it, we ad the difference to hashmap.
        """

        difference_map = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in difference_map: # if this condition is met, we've found the two values needed to add 
                return [difference_map[difference], i] 
            else:
                difference_map[nums[i]] = i
