class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slowSecond = 0
        while True:
            slowSecond = nums[slowSecond]
            slow = nums[slow]

            if slow == slowSecond:
                return slow
        
        


        