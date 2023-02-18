class staticArray:
    def __init__(self, arr = [0, 0, 0, 0], capacity = 4, length = 0) -> None:
        self.arr = arr
        self.capacity = capacity
        self.length = length
        # self.index = 0

    def insertEnd(self, value):
        self.value = value
        if self.length < self.capacity:
            self.arr[self.length] = self.value
            # self.index += 1
            self.length += 1

    def removeEnd(self):
        if self.length > 0:
            self.arr[-1]  = 0
            self.length -= 1

    def insertMiddle(self, index, value):
        self.index = index
        self.value = value
        if self.length > 0 and self.capacity > self.length:
            for i in range(self.capacity -2 ,self.index ,-1):
                self.arr[i+1] = self.arr[i]
            self.arr[i] = self.value
            self.length += 1

    def removeMiddle(self, index):
        self.index = index
        if self.length > 0:
            for i in range(self.index, self.length-1):
                self.arr[i] = self.arr[i + 1]
            self.length -= 1
    
    def printArr(self):
        print(self.arr)

  