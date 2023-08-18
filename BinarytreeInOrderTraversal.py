# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
out = []
class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        def inorderHelper(node: TreeNode):
            if node.left:
                inorderHelper(node.left)
            out.append(node.val)
            if node.right:
                inorderHelper(node.right)

        if root:
            inorderHelper(root)

        return out