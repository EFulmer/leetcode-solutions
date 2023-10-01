class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        vertices_by_incoming = {i: set() for i in range(n)}
        for u, v in edges:
            vertices_by_incoming[v].add(u)
        isolated = {k for k, v in vertices_by_incoming.items() if len(v) == 0}
        return isolated
