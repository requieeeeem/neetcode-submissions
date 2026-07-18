import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []
        for x, y in points:
            heap.append((math.sqrt(x**2 + y**2), [x, y])) #add (distance, [x, y]) into the heap

        heapq.heapify_max(heap) #heapify will compare distance first, then [x, y] (which doesn't matter)
        while len(heap) > k: #if heap > k, make it back to size
            heapq.heappop_max(heap)

        for distance, point in heap:
            result.append(point)
        
        return result
