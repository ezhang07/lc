# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res

        bfs = deque()
        bfs.append(root)
        res.append([root.val])

        while bfs:
            bfsVal = []
            for i in range(len(bfs)):
                node = bfs.popleft()
                if node.left:
                    bfs.append(node.left)
                    bfsVal.append(node.left.val)
                if node.right:
                    bfs.append(node.right)
                    bfsVal.append(node.right.val)
            if not bfs:
                return res
            res.append(bfsVal)
        
        return res

