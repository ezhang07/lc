# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: # base case for recursion
            return None

        # we wanna invert the tree, we do this by switching the values of left and right with each other

        temp = root.left
        root.left = root.right
        root.right = temp

        # we wanna then somehow initiate the recursion. in this case invertTree by itself doesn't rly return anything. we let it do its job and get to base case on both subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        # then the recursion has completed, and then we can return the root
        return root
        