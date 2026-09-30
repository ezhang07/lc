# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        variable keeping track of the diameter

        diameter -> essentially longest path formed from left right subtrees heights

        recursive approach

        helper, finding max depth of tree check diameter here as well
        """

        self.diameter = 0

        def dfs(curr):
            if not curr:
                return 0
            
            left_height = dfs(curr.left)
            right_height = dfs(curr.right)

            self.diameter = max(self.diameter, left_height + right_height)

            return max(left_height, right_height) + 1
        
        dfs(root)

        return self.diameter
        
        
