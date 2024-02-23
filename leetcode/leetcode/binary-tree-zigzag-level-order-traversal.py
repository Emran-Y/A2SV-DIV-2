# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nodes = {}
    def inorder(self,root,level_num):
        sign = 1

        if not root:
            sign *= -1
            return
        
        if level_num not in self.nodes:
            self.nodes[level_num] = []
        
        if level_num%2==0:
            self.nodes[level_num].append(root.val)
        else:
            self.nodes[level_num].insert(0,root.val)

        self.inorder(root.left,level_num + sign)
        self.inorder(root.right,level_num + sign)
        return

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.inorder(root,0)

        return [self.nodes[i] for i in sorted(self.nodes.keys())]
