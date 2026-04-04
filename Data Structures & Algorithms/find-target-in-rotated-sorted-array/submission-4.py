class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if nums[0] <= nums[-1]:
            l = 0
            r = len(nums)-1
            while l<=r:
                m = (l+r)//2

                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return m
            
            return -1

        l = 0
        r = len(nums)-1

        deflectionPointMin = 0

        while l <= r:
            m = (l+r)//2

            if nums[m] >= nums[0]:
                l = m + 1
            else:
                deflectionPointMin = m
                r = m - 1
        
        left = 0
        right = deflectionPointMin - 1
        while left <= right:
            m = (left+right)//2
            if nums[m] > target:
                right = m-1
            elif nums[m] < target:
                left = m+1
            else:
                return m
        
        leftRight = deflectionPointMin
        end = len(nums)-1
        while leftRight <= end:
            m = (leftRight+end)//2
            if nums[m] > target:
                end = m-1
            elif nums[m] < target:
                leftRight = m+1
            else:
                return m
        
        return -1
