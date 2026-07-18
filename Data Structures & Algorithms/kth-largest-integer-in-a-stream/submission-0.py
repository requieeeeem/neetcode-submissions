import heapq #we're using min heap, heapq is min heap by default
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums #store list as heap
        heapq.heapify(self.heap) #turns unordered list into a min heap without hard sorting it
        while len(self.heap) > k:
            heapq.heappop(self.heap) #trim off the smallest element until k largest remain

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0] #the k-largest
