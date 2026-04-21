class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True

        hashMap = { i:[] for i in range(n) }
        for n1, n2 in edges:
            hashMap[n1].append(n2)
            hashMap[n2].append(n1)

        visit = set()
        def dfs(node, parent):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in hashMap[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n