class Solution:
    def countTime( time: str) -> int:
        # msh = time[0]
        # lsh = time[1]
        # msm = time[3]
        # lsm = time[4]
        # count = 0
        # if msh =="?" and int(lsh) >3:
        #     count+=2
        # if msh =="?" and int(lsh) <=3:
        #     count+=3
        out = []
        rev = time[::-1].replace(":","")
        print(rev)
        for ind,ch in enumerate(rev):
            print(out)
            if rev[ind] == "?" and ind==0  and rev[ind+1] == "?":
                out.append(60)
                print("if 1")
            elif rev[ind] == "?" and ind==0  and rev[ind+1] != "?":
                out.append(10)
                print("if 2")
            elif rev[ind] == "?" and ind==1:
                out.append(6)
                print("if 3")
            if rev[ind] == "?" and ind==2  and rev[ind+1] == "?":
                out.append(24)
                print("if 4")
            elif rev[ind] == "?" and ind==2  and rev[ind+1] != "2":
                out.append(10)
                print("if 5")
            elif rev[ind] == "?" and ind==2 and rev[ind+1] == "2":
                out.append(4)
                print("if 6")
            elif rev[ind] == "?" and ind==3 and int(rev[ind-1])<2:
                out.append(3)
                print("if 7")
            elif ind ==3 and ch=="?":
                print(ind,ch,rev[ind])
                out.append(2)
                print("if 8")
        return out
    print(countTime(time = "??:??"))