class DynamicArray:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.arr = [0] * capacity
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size + 1 > self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        last = self.size - 1

        self.size -= 1
        return self.arr[last]

    def resize(self) -> None:
        self.capacity *= 2
        newArr = [0] * self.capacity

        for i in range(self.size):
            newArr[i] = self.arr[i]

        self.arr = newArr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity