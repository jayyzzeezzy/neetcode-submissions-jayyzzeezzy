class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parent = [i for i in range(N + 1)]
        rank = [1] * (N + 1)

        def find(n):
            if n != parent[n]:
                parent[n] = find(parent[n])
            return parent[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2: # p1 and p2 have the same parent root 
                return False 
                
            # perform union by rank, rewrite parent[], update rank[]
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True # if n1 is not connected to n2

        for n1, n2 in edges:
            if not union(n1, n2): # if false then there is a cycle
                return [n1, n2]