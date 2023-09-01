class Solution:
    def lastRemaining( n: int) -> int:
        c = 0
        n = [i for i in range(1,n+1)]
        while len(n)>1:
            if c%2==0:
                for i in range(0,len(n),2):
                    n.pop(i)
                    print("if ",i,n)
                c+=1
            elif c%2==1:
                for i in range(1,len(n)-2,2):
                    print("else",i)
                    n.pop(i)
                c+=1
            print(n)
        return n
    print(lastRemaining(n = 9))