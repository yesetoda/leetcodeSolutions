class Solution:
    def openLock( deadends: list[str], target: str) -> int:
        initial = ["0"]*4
        count1 = 0
        count2 = 0
        def rotate(val):
            return (val%6 if val<6 else 10-val,str(val))
        for i,ch in enumerate(target):
            print("".join(initial))
            if "".join(initial)==target:
                break
            initial[i] =  rotate(int(ch))[1]
            count1+=rotate(int(ch))[0] +1
            print(initial,count1)
        for i,ch in enumerate(target[::-1]):
            if "".join(initial)==target:
                break
            initial[i] =  rotate(int(ch))[1]
            count2+=rotate(int(ch))[0]+1
            print(initial,count2)
        return count1,count2
    openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0009")