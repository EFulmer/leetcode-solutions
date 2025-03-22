class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: make an adjacency list
        # (for ease of using standard DFS implementation)
        adjacency_list = make_adjacency_list(n=n, edges=edges)
        components = []
        # Step 2: for each node i:
        # If i hasn't been seen in any component yet,
        # do a DFS starting from it and note its component.
        for i in range(n):
            seen = any(i in edge for component in components for edge in component)
            if not seen:
                component_of_i = dfs_adjacency_list(
                    adjacency_list=adjacency_list, start=i,
                )
                components.append(component_of_i)
        # Step 3: for each component ID'd in step 2,
        # check whether it's complete.
        result = 0
        for component in components:
            result += is_component_complete(component)
        # Step 4: Return that number.
        return result


def make_adjacency_list(n: int, edges: list[list[int]]) -> dict[int, list[int]]:
    adjacency_list = {i: set() for i in range(n)}
    for edge in edges:
        start, end = edge
        adjacency_list[start].add(end)
        adjacency_list[end].add(start)
    return adjacency_list


def dfs_adjacency_list(
    adjacency_list: dict[int, set[int]], start: int
) -> set[tuple[int, int]]:
    queue = deque()
    seen = set()
    queue.append(start)
    edges = set()
    while len(queue) > 0:
        current = queue.popleft()
        seen.add(current)
        print(f"{current = }")
        for neighbor in adjacency_list[current]:
            current_edge = tuple(sorted((current, neighbor)))
            edges.add(current_edge)
            if neighbor not in seen:
                queue.append(neighbor)
    return edges


def is_component_complete(component: set[tuple[int, int]]) -> bool:
    nodes = set()
    for edge in component:
        nodes.add(edge[0])
        nodes.add(edge[1])
    m = len(nodes)
    needed_edges = (m * (m - 1)) / 2
    return needed_edges == len(component)
