class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    if i > j:
                        return [j,i]
                    else:
                        return [i,j]
                





    #at end, return answer with smaller index, using if statement
