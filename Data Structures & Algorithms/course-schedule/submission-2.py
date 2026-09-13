class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        course_prerequisites = {course: [] for course in range(numCourses)}


        def take(course, visited):
            if course in visited:
                return False

            # if preqrequisite is empty we can take it
            if not course_prerequisites[course]:
                return True

            visited.add(course)

            for pre in course_prerequisites[course]:
                if not take(pre, visited):
                    return False

            visited.remove(course)
            course_prerequisites[course] = []
            return True

        for course, pre in prerequisites:
            course_prerequisites[course].append(pre)


        for course in range(numCourses):
            if not take(course, set()):
                return False

        return True


