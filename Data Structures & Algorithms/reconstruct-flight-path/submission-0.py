class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = { src: [] for src, dst in tickets }

        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False

            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v): return True

                # backtrack decision
                adj[src].insert(i, v) # order specific
                res.pop()
            return False

        dfs("JFK")
        return res