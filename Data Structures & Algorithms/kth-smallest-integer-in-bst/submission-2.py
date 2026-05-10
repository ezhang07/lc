# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        self.cnt = 0

        def dfs(node):
            if self.cnt == k:
                return 
                
            if not node:
                return

            dfs(node.left)
            arr.append(node.val)
            self.cnt += 1
            dfs(node.right)

        dfs(root)
        
        return arr[k - 1]


        





