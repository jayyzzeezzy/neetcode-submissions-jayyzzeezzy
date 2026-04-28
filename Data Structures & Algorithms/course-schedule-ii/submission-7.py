class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = { i:[] for i in range(numCourses) }
        for course, pre in prerequisites:
            preMap[course].append(pre)

        visit, cycle = set(), set()
        res = []
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True

            cycle.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False

            cycle.remove(course)
            visit.add(course)
            res.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return res