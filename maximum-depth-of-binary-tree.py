# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stck=[(root,1)]
        mx=0
        while stck:

            a,b=stck.pop()

            mx=max(mx,b)

            if a.left:
                stck.append((a.left,b+1))
            if a.right:
                stck.append((a.right,b+1))
        return mx


