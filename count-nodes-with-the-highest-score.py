class Solution(object):
    def countHighestScoreNodes(self, parents):
        """
        :type parents: List[int]
        :rtype: int
        """
        size = len(parents)
        counter = [[] for j in range(size)]

        childs = [[] for i in range(size)]
        for i in range(size):
            if(i != 0) : childs[parents[i]].append(i)

        def traverse(root):
            ans = 0
            for i in childs[root]:
                num = traverse(i)
                counter[root].append(num)
                ans += num
            return ans + 1
        
        traverse(0)
        ans = 0
        cnt = 0
        ansList = []
        for i in counter:
            if(len(i) == 0):
                num = size - 1
            elif(len(i) == 1):
                num = i[0] * max(1, (size - i[0] - 1))
            else:
                num = i[0] * i[1] * max(1, (size - i[0] - i[1] - 1))
            ansList.append(num)
            ans = max(ans, num)

        for i in ansList:
            if(ans == i):
                cnt += 1

        return cnt