# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        arr = [[] for i in range(20)]

        def traverse(root, depth):
            if(root == None):
                return

            arr[depth].append(root.val)
            traverse(root.left, depth + 1)
            traverse(root.right, depth + 1)
            

        traverse(root, 0)
        for i in range(len(arr)):
            if(i % 2 == 1):
                arr[i].reverse()
        newArr = []

        for i in arr:
            newArr += i

        def create(root, idx):
            if(root == None):
                return
            
            root.val = newArr[idx - 1]
            create(root.left, idx * 2)
            create(root.right, idx * 2 + 1)

        create(root, 1)

        return root