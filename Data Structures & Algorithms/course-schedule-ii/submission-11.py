class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for course, pre in prerequisites:
            adjList[course].append(pre)

        visit, cycle = set(), set()
        res = []
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True

            cycle.add(course)
            for pre in adjList[course]:
                if not dfs(pre):
                    return False

            cycle.remove(course)
            res.append(course)
            visit.add(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []

        return res