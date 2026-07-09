class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root: 
            nextLayer = deque()
            nextLayer.append(root)
            while nextLayer:
                # the right most node will be on the right, so we can pop from the right
                tmp = []
                rightmost = nextLayer.pop()
                result.append(rightmost.val)
                # put the rightmost back into the queue all the way to at the back
                nextLayer.append(rightmost)
                while nextLayer:
                    tmp.append(nextLayer.popleft())
                for node in tmp:
                    if node.left:
                        nextLayer.append(node.left)
                    if node.right:
                        nextLayer.append(node.right)
        return result