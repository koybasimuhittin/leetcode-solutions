# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        def search(root, val):
            if(not root == None):
                if(root.val == val):
                    return root
                
                left = search(root.left, val)
                right = search(root.right, val)

                if(left != None):
                    return left
                elif(right != None):
                    return right
            return None

        return search(root, val)
        