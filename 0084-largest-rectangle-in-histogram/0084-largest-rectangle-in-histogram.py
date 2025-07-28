class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_area=0
        n=len(heights)

        for i in range(n):
            current_height=heights[i]

            while stack and current_height<heights[stack[-1]]:
                top=stack.pop()

                if stack:
                    width=i-stack[-1]-1
                else:
                    width=i
            
                area=heights[top]*width
                max_area=max(area,max_area)
            stack.append(i)
            
        while stack:
            top=stack.pop()

            if stack:
                width=n-stack[-1]-1
            else:
                width=n
            
            area=heights[top]*width
            max_area=max(area,max_area)
        return max_area
       