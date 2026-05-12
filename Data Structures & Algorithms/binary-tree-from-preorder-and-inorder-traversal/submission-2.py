# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {}

        # add values from inorder to map, values : index
        for i, val in enumerate(inorder):
            inorderMap[val] = i
        
        self.preorderIndex = 0

        def dfs(l, r):
            if l > r:
                return None
            
            val = preorder[self.preorderIndex]
            node = TreeNode(val)
            mid = inorderMap[val]
            self.preorderIndex += 1

            node.left = dfs(l, mid - 1)
            node.right = dfs(mid + 1, r) 

            return node
        
        return dfs(0, len(preorder) - 1)





