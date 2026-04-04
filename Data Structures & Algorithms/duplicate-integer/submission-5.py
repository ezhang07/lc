class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueElements = set()

        for n in nums:
            if n in uniqueElements:
                return True
            else:
                uniqueElements.add(n)

        return False

