class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adjacency list
        preMap  = { c:[] for c in range(numCourses) }
        for course, pre in prerequisites:
            preMap[course].append(pre)

        visit, cycle = set(), set()
        output = []
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True

            # check cycle
            cycle.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False
            cycle.remove(course)

            # mark visited
            visit.add(course)
            # add to output
            output.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c): 
                return []
        return output