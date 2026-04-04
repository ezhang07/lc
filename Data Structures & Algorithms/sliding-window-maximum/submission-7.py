class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l = 0
        r = 0
        res = []

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if r+1 >= k:
                res.append(nums[q[0]])
                l+=1
            r+=1

        return res

            # need to have a case checking for if nums[r] bigger than, and smaller than rightmost element
            # if bigger, keep on popping the right, until it isn't then we append
            # if smaller, than just append
            # if no values in the queue,then can just add the value
            # also check if the frontmost index is still in the window?
