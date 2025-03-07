# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], t: int) -> List[List[int]]:
        if not root:
            return []
        else:
            stck=[(root,root.val,[root.val])]
            al=[]

            while stck:

                a,s,path=stck.pop()

                if s==t and not a.left and not a.right:
                    al.append(path)

                if a.right:
                    stck.append((a.right,s+a.right.val,path+[a.right.val]))
                if a.left:
                    stck.append((a.left,s+a.left.val,path+[a.left.val]))
            
            return al
                
            
            

        




        
