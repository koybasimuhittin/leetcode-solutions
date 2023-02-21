# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """

        maxVal = root.val

        def calculateNodeNumber(root):
            if(root == None):
                return -1
        
            left = calculateNodeNumber(root.left)
            right = calculateNodeNumber(root.right)
            return max(left, max(right, root.val))

        maxVal = max(maxVal, calculateNodeNumber(root))
        adjecancyList = [[] for i in range(maxVal + 1)]
        visited = [False for i in range(maxVal + 1)]

        def traverse(root):
            if(root == None):
                return

            if(root.left != None):
                adjecancyList[root.val].append(root.left.val)
                adjecancyList[root.left.val].append(root.val)
            
            if(root.right != None):
                adjecancyList[root.val].append(root.right.val)
                adjecancyList[root.right.val].append(root.val)

            traverse(root.left)
            traverse(root.right)

        def findFurthestToStart(root):
            visited[root] = True
            ans = 0
            for i in adjecancyList[root]:
                if(visited[i] == False):
                    ans = max(ans, findFurthestToStart(i) + 1)
            return ans

        traverse(root)

        return findFurthestToStart(start)