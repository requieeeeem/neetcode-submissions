class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1) #making sure first list is always shorter
        totalPartition = (len(nums1) + len(nums2) + 1) // 2
        #left and right = number of elements to the left/right of partition, NOT INDEX
        left = 0
        right = len(nums1)
        while left <= right:
            partition1 = (right + left) // 2 #midpoint of left and right
            partition2 = totalPartition - partition1
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1] #nothing at the left of index 0
            minRight1 = float('inf') if partition1 == len(nums1) else nums1[partition1] #nothing at the right of last index
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == len(nums2) else nums2[partition2]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                #found the partition
                if (len(nums1) + len(nums2)) % 2 == 0: #even, return average of 2
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else: #odd, return max between 2 leftmosts
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                right = partition1 - 1
            else:
                left = partition1 + 1

        