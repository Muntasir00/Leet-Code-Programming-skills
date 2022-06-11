class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        leaves_sum = 0
        if root is None:
            return 0
        if root.left is not None and root.left.left is None and root.left.right is None:
            leaves_sum += root.left.val
        else:
            leaves_sum+= self.sumOfLeftLeaves(root.left)
        if root.right is not None:
            if root.right.left is not None or root.right.right is not None:
                leaves_sum+= self.sumOfLeftLeaves(root.right)
        
        return leaves_sum