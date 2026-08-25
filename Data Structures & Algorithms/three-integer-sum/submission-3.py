class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for i in range(len(nums)): # i will be the value we're going to precompute
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i] * -1
            l, r = i + 1, len(nums) - 1
            while l < r:
                addition = nums[l] + nums[r]
                if addition == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                if addition > target:
                    r -= 1
                if addition < target:
                    l += 1
        
        return res


                

            


