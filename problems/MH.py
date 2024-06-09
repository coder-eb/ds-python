from DS.MaxHeap import MaxHeap

def stream_max(nums):
    max_heap = MaxHeap()
    stream_max = []
    for num in nums:
        max_heap.insert(num)
        stream_max.append(max_heap.heap[0])
    return stream_max

def find_kth_smallest(nums, k):
    max_heap = MaxHeap()
    for num in nums:
        max_heap.insert(num)
        if len(max_heap.heap) > k:
            max_heap.remove()
    return max_heap.remove()