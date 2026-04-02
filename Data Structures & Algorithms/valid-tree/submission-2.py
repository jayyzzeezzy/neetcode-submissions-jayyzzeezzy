class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        edgeMap = { i:[] for i in range(n) }
        for n1, n2 in edges:
            edgeMap[n1].append(n2)
            edgeMap[n2].append(n1)

        visit = set()
        def dfs(node, parent):
            if node in visit:
                return False

            visit.add(node)
            for nei in edgeMap[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False

            return True

        return dfs(0, -1) and len(visit) == n