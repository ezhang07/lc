# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        - in order traversal, since we are alwasy checking left subtree first,
        the root node/middle is found in the middle of the array.
        - the root node value can be found in the preorder, as it always checks root
        before the subtrees, so we know it through the first value in the array


        - inorder: root node found in middle
        - preorder: root node found in beginning
        use preorder beginning value to find middle index in inorder.
        anything before index is left subtree, anything after is right

        """



        if not preorder or not inorder:
            return None
        

        node = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        node.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return node





