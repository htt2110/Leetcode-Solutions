'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
''' 

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    
    ls = []
    ls.extend(nums1)
    ls.extend(nums2)
    ls.sort()
    l = len(ls)
    i = int((l-1)/2)
    if l%2 == 0:
        return float((ls[i] + ls[i+1])/2)
    else:
        return float(ls[i])