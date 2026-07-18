import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums 
        heapq.heapify(heap) #min heap, smallest number is root
        while len(heap) > k: #trim off until k largest element is at root
            heapq.heappop(heap)
        
        return heap[0] #return root