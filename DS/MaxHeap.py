class MaxHeap:
    def __init__(self, value=[]):
        self.heap = value
    
    def _left_child(self, index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current_index = len(self.heap) - 1

        # breaks when top is reached
        while current_index > 0: 
            parent_index = self._parent(current_index)
            if self.heap[parent_index] > self.heap[current_index]:
                break # Heap is already valid
            self._swap(parent_index, current_index)
            current_index = parent_index
        return True
    
    def __str__(self) -> str:
        return self.heap.__str__()

