from DS.Heap import Heap


class MinHeap(Heap):
    def _sink_down(self, index):
        min_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and self.heap[left_index] < self.heap[min_index]:
                min_index = left_index
            if right_index < len(self.heap) and self.heap[right_index] < self.heap[min_index]:
                min_index = right_index
            
            # Heap is valid if current index is the max index
            if index == min_index:
                return
            
            self._swap(index, min_index)
            index = min_index
        

    def insert(self, value):
        self.heap.append(value)
        current_index = len(self.heap) - 1

        # breaks when top is reached
        while current_index > 0: 
            parent_index = self._parent(current_index)
            if self.heap[parent_index] < self.heap[current_index]:
                break # Heap is already valid
            self._swap(parent_index, current_index)
            current_index = parent_index
        return True
    
    def remove(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return min_value

