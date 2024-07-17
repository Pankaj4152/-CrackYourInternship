class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        max_area = 0

        while left < right:
            current_area = min(height[left], height[right]) * (right - left) 

            if current_area > max_area:
                max_area = current_area

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return max_area
