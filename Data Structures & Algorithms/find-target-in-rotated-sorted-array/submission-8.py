class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1 
        minimumIndex = 0

        while l <= r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else: # nums[m] == nums[r], signifying that we are at the minimum. essentially the pivot point
                minimumIndex = m 
                break
        
        if minimumIndex == 0: # not rotated whatsoever
            l, r = 0, len(nums) - 1
        elif target >= nums[0] and target <= nums[minimumIndex - 1]:
            l = 0
            r = minimumIndex - 1
        else:
            l = minimumIndex
            r = len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1

                    