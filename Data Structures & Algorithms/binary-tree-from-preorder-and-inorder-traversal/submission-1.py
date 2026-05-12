# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # make the current node, using the fact that preorder traverses root node first
        node = TreeNode(preorder[0])

        # using that info, also find partition of left and right subtrees, within inorder
        mid = inorder.index(preorder[0])

        # recursive calls on left and right nodes, making sublists for the preorder and inorder
        node.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        node.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        
        return node





