# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    isBalance = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.getHeight(root)

        return self.isBalance

    def getHeight(self, root):   
        if not root:
            return 0
        
        leftH = self.getHeight(root.left)
        rightH = self.getHeight(root.right)

        if abs(leftH-rightH) > 1:
            self.isBalance = False
        
        return max(leftH, rightH) + 1