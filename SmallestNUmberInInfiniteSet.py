class SmallestInfiniteSet:

    def __init__(self):
        self.list = [i for i in range(1000+1)]
        

    def popSmallest(self) -> int:
        return self.list.pop(min(self.list))
        

    def addBack(self, num: int) -> None:
        if num not  in self.list:
            for i in range(1,1000+1):
                if i not in self.list:
                    self.list.insert(i,i)
            



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)