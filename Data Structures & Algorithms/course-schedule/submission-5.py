class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for course, pre in prerequisites:
            adj[course].append(pre)

        visited, path = set(), set()
        def dfs(course):
            if course in path:
                return False

            if course in visited:
                return True

            visited.add(course)
            path.add(course)

            for neighbor in adj[course]:
                if not dfs(neighbor):
                    return False

            path.remove(course)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True