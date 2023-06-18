class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        r = len(nums) -1
        l = 0 
        while l <= r:
    
            mid = l + (r - l) // 2
    
            # Check if x is present at mid
            if nums[mid] == target:
                return mid
    
            # If x is greater, ignore left half
            elif nums[mid] < target:
                l = mid + 1
    
            # If x is smaller, ignore right half
            else:
                r = mid - 1

        return l

