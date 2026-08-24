class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            add = numbers[l] + numbers[r]
            if add == target:
                return [l + 1, r + 1]
            if add > target: # wanna go lower target value
                r -= 1
            elif add < target: # wanna go higher target value
                l += 1
        