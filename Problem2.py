# Problem 2
#Course Schedule (https://leetcode.com/problems/course-schedule/)


# Approach
# To solve this using Topological Sort, create a indegrees list of size numCourses. Traverse through prerequisites list and get the dependencies for each course and update it in indegrees list
# Similarly, if course is already present in hmap, add the dependent course to the list value. Create queue and add all the courses with 0 dependencies. Traverse through the queue, pop leftmost element. 
# Check if course is in hmap, if yes, reduce values for all the corresponding dependant courses. If course becomes 0 in indegrees, add it to the queue. check the count, if count == numCourses , return True. Once outside loop, return False

# Time Complexity: O(v+e)
# Space Complexity : O(v+e)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for i in range(numCourses)]
        count = 0
        hmap = {}
        for i in prerequisites:
            indegrees[i[0]] += 1
            if i[1] in hmap:
                hmap[i[1]].append(i[0])
            else:
                hmap[i[1]] = [i[0]]
    
        queue = deque()
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)
                count += 1
        
        if count == numCourses:
            return True

        while queue:
            course = queue.popleft()
        
            if course in hmap:
                li = hmap[course]
                if li:
                    for i in li:
                        indegrees[i] -= 1
                        if indegrees[i] == 0:
                            queue.append(i)
                            count += 1
                            if count == numCourses:
                                return True

        
        return False