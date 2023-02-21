class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        visited = {}
        occuranceVisited = {}

        for i in arr:
            visited[i] = visited.get(i, 0) + 1
        
        for key in visited:
            print(key)
            if(occuranceVisited.get(visited[key], False)):
                return False
            occuranceVisited[visited[key]] = True
        return True