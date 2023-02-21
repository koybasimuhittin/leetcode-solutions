# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def traverse(root):
            if(root == None):
                return
            
            left = root.left
            right = root.right
            root.left = right
            root.right = left
            traverse(left)
            traverse(right)

        traverse(root)

        return root 