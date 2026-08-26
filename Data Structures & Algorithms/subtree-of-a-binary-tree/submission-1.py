class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return isSame(p.left, q.left) and isSame(p.right, q.right)
        
        # Base case: an empty tree has no non-empty subtrees
        if not root:
            return False
        
        # If the trees match from this node, we are done
        if isSame(root, subRoot):
            return True
        
        # Otherwise, check recursively in left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)