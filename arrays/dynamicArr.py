# create a dynamic array class
import ctypes  # To create low-level arrays
class MyArray:
    def __init__(self, size):
        self.length = 0
        self.capacity = size
        self.array = self._make_array(self.capacity)

    def __len__(self):
        return self.length
    
    def __getItem__(self,index):
        return self.array[index]

    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for i in range(self.length):
            new_array[i] = self.array[i]
        #change the reference
        self.array = new_array
        self.capacity = new_capacity

    def append(self,item):
        if self.length == self.capacity:
            # need to double the size 
            self._resize(2 * self.capacity)  # Double the capacity if full
        self.array[self.length] = item
        self.length += 1

    def delete(self,index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        # shift the elemeent left to fill the gap
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i+1]

        # set last element to none
        self.array[self.length-1] = None
        self.length -= 1


        


    def _make_array(self, capacity):
        """Create a low-level array with given capacity."""
        return (capacity * ctypes.py_object)()
    
    def __str__(self):
        result = []
        for i in range(self.length):
            result.append(str(self.array[i]))
        return "[" + ", ".join(result) + "]"


#usage 
# Example usage:
arr = MyArray(3)
arr.append(1)
arr.append(2)
arr.append(3)
arr.append(4)  # Resize should happen here

print("Array contents after appending:", arr)  # Output: [1, 2, 3, 4]
arr.delete(1)  # Delete item at index 1 (removes '2')
print("Array contents after deleting index 1:", arr)  # Output: [1, 3, 4]

arr.delete(2)  # Delete item at index 2 (removes '4')
print("Array contents after deleting index 2:", arr)  # Output: [1, 3]