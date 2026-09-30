# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        base case: no root, return 0

        stack
        maxDepth

        while stack:
            pop node from stack (given depth and node)
            check maxdepth

            get children, append to stack as well as its depth
        """

        if not root:
            return 0
        
        stack = [(root, 1)]
        maxDepth = 1

        while stack:
            node, curDepth = stack.pop()
            maxDepth = max(maxDepth, curDepth)

            if node.left:
                stack.append((node.left, curDepth + 1))
            if node.right:
                stack.append((node.right, curDepth + 1))
        
        return maxDepth
        
