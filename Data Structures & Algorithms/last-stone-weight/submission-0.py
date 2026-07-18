import heapq #using reverse heapq for max heap
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(heap) #turns stones list into a max heap

        while len(heap) >= 2:
            stone1 = heapq.heappop_max(heap) #get 2 heaviest stone
            stone2 = heapq.heappop_max(heap)
            if stone1 == stone2: #comparing them
                continue
            else: #stone 1 will always be equal to or heavier than stone 2 (max heap)
                newStone = stone1 - stone2
                heapq.heappush_max(heap, newStone)

        return heap[0] if len(heap) > 0 else 0 #return stone if there is any left, 0 if none
