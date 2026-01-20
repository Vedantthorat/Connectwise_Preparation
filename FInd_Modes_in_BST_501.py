# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        self.curr_val = None
        self.curr_count = 0
        self.max_count = 0
        self.modes = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.curr_val == node.val:
                self.curr_count +=1
            else:
                self.curr_val = node.val
                self.curr_count = 1
            
            if self.curr_count > self.max_count:
                self.max_count = self.curr_count
                self.modes = [node.val]

            elif self.curr_count ==  self.max_count:
                self.modes.append(node.val)

            inorder(node.right)
        inorder(root)
        return self.modes
