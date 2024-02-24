# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.temp = []
        self.ans = []
    def order(self,root):
        if not root:
            return 
        if root and not root.left and not root.right:
            self.temp.append(root.val)
            self.ans.append(self.temp[:])
            self.temp.pop()
            return
        self.temp.append(root.val)
        self.order(root.left)
        self.order(root.right)

        if self.temp: self.temp.pop()
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.order(root)

        max_ = 0

        for i in self.ans:
            max_ = max(max_,max(i) - min(i))
        return max_