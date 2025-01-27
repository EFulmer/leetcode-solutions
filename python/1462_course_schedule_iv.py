class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]]
    ) -> List[bool]:
        # Like usual we can short-circuit on a base case.
        if len(prerequisites) == 0:
            return [False] * len(queries)
        # Modified Kahn's algorithm.
        # https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm
        adjacent = defaultdict(list)
        # In Kahn's, we need to track the in-degree of each vertex.
        # (here, this is the number of prerequistes):
        num_prerequisites = [0] * numCourses

        for course, prerequisite in prerequisites:
            adjacent[course].append(prerequisite)
            num_prerequisites[prerequisite] += 1

        # Collect all the nodes with no incoming edge, in other words,
        # in-degree zero.
        # In our "business logic", that's courses without
        # prerequisites. Called S in the Wikipedia article:
        s = deque()
        for i, in_degree in enumerate(num_prerequisites):
            if in_degree == 0:
                s.append(i)

        # Keep a mapping of each course's number to a set of its'
        # prereqs.
        prerequisites_by_course = defaultdict(set)
        while s:
            current_course = s.popleft()
            for node in adjacent[current_course]:
                # Add the current node to prerequisites_by_course,
                # then traverse its adjacents
                # (in other words, its prereqs)
                prerequisites_by_course[node].add(current_course)
                for prerequisite in prerequisites_by_course[current_course]:
                    prerequisites_by_course[node].add(prerequisite)
                num_prerequisites[node] -= 1
                if num_prerequisites[node] == 0:
                    s.append(node)

        # With each course's prerequisites collected, we can now answer
        # the queries by looking at the dictionary we've created.
        result = [False] * len(queries)
        for i, (course_1, course_2) in enumerate(queries):
            if course_1 in prerequisites_by_course[course_2]:
                result[i] = True
        return result
