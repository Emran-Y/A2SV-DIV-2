# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        arr = []
        temp = ''
        t = root.val
        a = []
        def order(root):
            nonlocal temp
            if not root:
                return 
            if root and not root.left and not root.right:
                temp+=str(root.val)
                arr.append(temp)
                temp = temp[:len(temp) - 1]
                return 
            
            temp+=str(root.val)
            a.append(root.val)
            order(root.left)
            order(root.right)
            temp = temp[:len(temp) - 1]

            return

        order(root)
        return sum([int(i) for i in arr])

