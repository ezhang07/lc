# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        - base case, returns true
        - last point suggests that we should use recursion
        - we want to check whether 
        left subtree's values are less than node,
        right rubtree's values larger than node
        """

        def dfs(node, lower, upper):
            if not node:
                return True
            
            if node.val <= lower or node.val >= upper:
                return False
            
            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)
        
        return dfs(root, -1001, 1001)

                
