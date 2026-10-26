class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        course_prerequisites = {course: [] for course in range(numCourses)  }
        for course, pre in prerequisites:
            course_prerequisites[course].append(pre)

        visited = set()
        def take(course):
            if course in visited:
                return False

            if not course_prerequisites[course]:
                return True

            visited.add(course)
            for pre in course_prerequisites[course]:
                if not take(pre):
                    return False

            visited.remove(course)
            course_prerequisites[course] = []
            return True


        for i in range(numCourses):
            if not take(i):
                return False


        return True



        