# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.table = {}
    def order(self,root,row,col):
        if not root:
            return
        if col not in self.table:
            self.table[col] = []
        self.table[col].append((row,root.val))

        self.order(root.left,row + 1 , col - 1)
        self.order(root.right,row + 1, col + 1)
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.order(root,0,0)
        ans = []

        for i in sorted(self.table.keys()):
            nodes = [val for row,val in sorted(self.table[i],key=lambda x:(x[0],x[1]))]
            ans.append(nodes)
        return ans