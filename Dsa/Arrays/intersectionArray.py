# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        result = []
        while i < len(nums1) and j < len(nums2): # while i and j are within the bounds of the arrays 
            if nums1[i] == nums2[j]: # if the values are equal, add to result and increment both i and j
                result.append(nums1[i]) 
                i += 1
                j += 1
            elif nums1[i] < nums2[j]: # if the value in nums1 is less than the value in nums2, increment i because we want to find the next value in nums1 that is equal to the value in nums2
                i += 1
            else: # if the value in nums2 is less than the value in nums1, increment j because we want to find the next value in nums2 that is equal to the value in nums1
                j += 1
        return result
    