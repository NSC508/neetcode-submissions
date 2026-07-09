# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        global result
        result = 0 
        
        def isGoodNode(node, maxSoFar):
            global result  # Must declare global inside this scope too
            if node.val >= maxSoFar: 
                result += 1
                maxSoFar = node.val
            
            if node.left: isGoodNode(node.left, maxSoFar)
            if node.right: isGoodNode(node.right, maxSoFar)

        isGoodNode(root, root.val)
        return result