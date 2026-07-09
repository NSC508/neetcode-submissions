class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root:
            nextLayer = deque()
            nextLayer.append(root)

            while nextLayer:
                tmp = []
                layer = []
                while nextLayer:
                    tmp.append(nextLayer.popleft())
                
                for node in tmp:
                    layer.append(node.val)
                    if node.left:
                        nextLayer.append(node.left)
                    if node.right:
                        nextLayer.append(node.right)
                
                result.append(layer)

        return result