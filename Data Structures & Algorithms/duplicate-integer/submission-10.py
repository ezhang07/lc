class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        hashset approach
        -> keeps count of the values iterated over
        """

        seenValues = set()

        for n in nums:
            if n in seenValues:
                return True
            seenValues.add(n)
        
        return False
            