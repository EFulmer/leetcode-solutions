class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Using Kahn's algo.
        # 1. Build graph and in-degree list:
        in_degrees = [0] * numCourses
        adjacency_list = {i : [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            in_degrees[course] += 1
            adjacency_list[prereq].append(course)

        # 2. Make a list of the courses without prereqs
        #    (S in the Wikipedia definition):
        no_prereqs = deque([i for i in range(numCourses) if in_degrees[i] == 0])

        # 3. Topological sort:
        # 3a. Instantiate topological sort list (L):
        topological_sort = []
        while no_prereqs:
            # 3b. Take a node from the set of nodes with in-degree 0
            #     and add it to L.
            current_course = no_prereqs.popleft()
            topological_sort.append(current_course)

            # 3c. Remove this course from our graph representation, and
            #     add any neighbors to S if they fit the criteria (no
            #     more inbound edges)
            for neighbor in adjacency_list[current_course]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    no_prereqs.append(neighbor)

        # Our criteria here is that we can reach every node, given by
        # numCourses. So the length of our topological sort should be
        # equal to numCourses.
        return len(topological_sort) == numCourses
