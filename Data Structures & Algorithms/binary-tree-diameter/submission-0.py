# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxD = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.getD(root)
        return self.maxD

    def getD(self, root):
        if not root:
            return 0
        
        leftH = self.getD(root.left)
        rightH = self.getD(root.right)
        
        currD = leftH + rightH
        if currD > self.maxD:
            self.maxD = currD
        
        return max(leftH, rightH) + 1


