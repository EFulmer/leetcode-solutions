# This could be significantly refactored...

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        """Compute the number of unique paths in a grid.
        """
        solutions = []
        start = self.find_start(grid)
        obstacles = self.find_all(grid, -1)
        self.backtrack(
            solutions=solutions,
            candidate_solution=[start],
            k=0,
            start=start,
            end=self.find_end(grid),
            grid=grid,
            obstacles=obstacles,
        )
        return len(solutions)

    def backtrack(
        self,
        solutions: List,
        candidate_solution: List,
        k: int,
        start: int,
        end: int,
        grid: List[List[int]],
        obstacles: List[List[int]],
    ):
        """Backtracking solution for the problem.

        Args:
            solutions: All complete solutions.
            candidate_solution: Possible current solution, investigation in progress.
                ("a" in Skiena)
            k: Head (most recently added item) of the solution we're inspecting presently.
            start: Starting coordinate of the path in the grid.
            end: Ending coordinate of the path in the grid.
            grid: The grid itself.
        """
        # taken from Skiena, original in C
        if self.is_a_solution(a=candidate_solution, grid=grid):
            solutions.append(candidate_solution)
        else:
            k += 1
            next_possible_candidates = self.construct_candidates(
                solution_in_progress=candidate_solution,
                k=k,
                start=start,
                end=end,
                grid=grid,
                obstacles=obstacles,
            )
            for candidate in next_possible_candidates:
                self.backtrack(
                    solutions=solutions,
                    candidate_solution=candidate_solution + [candidate],
                    k=k,
                    start=start,
                    end=end,
                    grid=grid,
                    obstacles=obstacles,
                )

    def construct_candidates(
        self,
        solution_in_progress: List,
        k: int,
        start: List[int],
        end: List[int],
        grid: List[List[int]],
        obstacles: List[List[int]],
    ) -> List[List[int]]:
        # Our current candidate from a co-ordinate position K (or solutions[K]) are:
        # any square 1 distance from S[K], that has not been visited yet, is in the grid, and is not an obstacle (-1)
        # we can also figure out the length of a "complete" candidate solution by subtracting the # of obstacles (TODO)
        i, j = solution_in_progress[k-1]
        candidates = []

        # if (i-1, j) fits, add it:
        if i-1 >= 0 and (i-1, j) not in solution_in_progress:
            if grid[i-1][j] != -1:
                candidates.append((i-1, j))
        # if (i+1, j) fits, add it:
        if i+1 < len(grid) and (i+1, j) not in solution_in_progress:
            if grid[i+1][j] != -1:
                candidates.append((i+1, j))
        # if (i, j-1) fits, add it:
        if j-1 >= 0 and (i, j-1) not in solution_in_progress:
            if grid[i][j-1] != -1:
                candidates.append((i, j-1))
        # if (i, j+1) fits, add it:
        if j+1 < len(grid[0]) and (i, j+1) not in solution_in_progress:
            if grid[i][j+1] != -1:
                candidates.append((i, j+1))
        return candidates

    def is_a_solution(self, a: List[List[int]], **kwargs) -> bool:
        # A solution will need to satisfy the following conditions:
        # 1. first element is the start square
        # 2. last element is the end square
        # 3. none of the elements are coordinates of an obstacle
        # 4. The n-th element must be adjacent to the (n-1)th and (n+1)-th
        # 5. All non obstacle squares are traversed exactly once
        # Check condition 1:
        start = self.find_start(kwargs['grid'])
        if start != a[0]:
            return False
        # Check condiion 2:
        end = self.find_end(kwargs['grid'])
        if end != a[-1]:
            return False
        obstacles_on_the_path = [
            kwargs['grid'][i][j] == -1
            for (i, j) in a
        ]
        if any(obstacles_on_the_path):
            return False
        # Check condition 4:
        for (p1, p2) in zip(a[:-1], a[1:]):
            # Definition of adjacency on this discrete 2D grid:
            # Points (A, B) are adjacent if one coordinate of A is one off from one coordinate of B and the other coordinate of A matches the other coordinate of B
            if not self.adjacent(p1, p2):
                return False
        # Check condition 5
        obstacles = self.find_all(kwargs['grid'], -1)
        if len(a) != (len(kwargs['grid']) * len(kwargs['grid'][0]) - len(obstacles)):
            return False
        return True

    def adjacent(self, p1, p2) -> bool:
        if ((abs(p1[0] - p2[0]) == 1 and abs(p1[1] - p2[1]) == 0) or (abs(p1[1] - p2[1]) == 1 and abs(p1[0] - p2[0]) == 0)):
            return True
        else:
            return False

    def find_start(self, grid: List[List[int]]) -> Tuple[int, int]:
        return self.find_one(grid=grid, target=1)

    def find_end(self, grid: List[List[int]]) -> Tuple[int, int]:
        return self.find_one(grid=grid, target=2)

    def find_one(self, grid: List[List[int]], target: int) -> Tuple[int, int]:
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if grid[i][j] == target:
                    return (i, j)

    def find_all(self, grid: List[List[int]], target: int) -> List[Tuple[int, int]]:
        result = []
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if grid[i][j] == target:
                    result.append((i, j))
        return resultt
