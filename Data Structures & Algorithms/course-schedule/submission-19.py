class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            adjList[course].append(pre)

        visit = set()
        def dfs(course):
            if course in visit:
                return False
            
            # return True early
            if adjList[course] == []:
                return True
            
            visit.add(course)
            for pre in adjList[course]:
                if not dfs(pre):
                    return False

            adjList[course] = []
            visit.remove(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True