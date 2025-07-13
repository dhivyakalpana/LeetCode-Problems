class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
       graph=defaultdict(list)
       in_degree=[0]*numCourses

       for course,prev in prerequisites:
        graph[prev].append(course)
        in_degree[course]+=1

       queue=deque([i for i in range(numCourses) if in_degree[i]==0])
       completed_course=0

       while queue:
        course=queue.popleft()
        completed_course+=1

        for neighbor in graph[course]:
            in_degree[neighbor]-=1
            if in_degree[neighbor]==0:
                queue.append(neighbor)
                
       return completed_course==numCourses



