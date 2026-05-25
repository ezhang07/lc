# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # global variable recording the max sum
        self.res = root.val

        # helper function, returning max path for one node (including 0/1 children)
        def dfs(root):
            # checking whether current node is null, if null, return 0
            if not root:
                return 0
            
            # post order traversal. if children are negative, will default to 0 instead (basically not including that child)
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)

            # update max sum, checking the sum of root with its left and right subtrees
            self.res = max(self.res, root.val + left + right)

            # return larger sum between root with left child vs right child
            return max(root.val + left, root.val + right)

        dfs(root)

        return self.res

        

