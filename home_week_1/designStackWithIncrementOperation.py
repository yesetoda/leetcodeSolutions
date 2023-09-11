class CustomStack:

    def __init__(self, maxSize: int):
        self.limit = maxSize
        self.stack = []
        
    def push(self, x: int) -> None:
        if len(self.stack)<self.limit:
            self.stack.append(x)
            
    def pop(self) -> int:
        return self.stack.pop() if self.stack else -1
        
    def increment(self, k: int, val: int) -> None:
        
        for i in range(min(k,len(self.stack))):
                if self.stack[i]:
                    self.stack[i]+=val
        print(self.stack)

     
# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
print(a := CustomStack(30))
print(a.pop())
print(a.increment(3,40))
print(a.push(30))
print(a.increment(4,63))
print(a.increment(2,79))
print(a.increment(5,57))
print(a.pop())
print(a.increment(5,23))





# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)