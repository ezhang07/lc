class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        interval must have a start and end
        [1,2] and [2, 3] become [1,3]
        non-empty list

        sort by starting interval index 
        res array, holding intervals

        need to compare ending of last interval in res array
        with the start of current interval we are at
        check overlap

        if there is: change the existing interval in res (its end)
        if there isn't: append new interval
        """

        intervals.sort(key=lambda interval: interval[0])
        res = []

        for i in intervals:
            if not res or res[-1][1] < i[0]:   # no overlap, start of curr > ending of last res
                res.append(i)
            else:
                res[-1][1] = max(i[1], res[-1][1])
        
        return res
        

                


