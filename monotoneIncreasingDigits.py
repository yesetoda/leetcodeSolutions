class Solution:
    def monotoneIncreasingDigits(n: int) -> int:
        # srt = "".join(sorted(str(n)))
        # print(srt)
            ind = -1
        # if n == int(srt):
        #     return n
        # else:
            s = str(n)
            srt = "".join(sorted(str(n)))
            if n == int(srt):
                return n
            # while n!= int(srt):
            while True:
                # print(n,ind)
                # print(n,str(n),str(n)[ind],int(str(n)[ind])+1,(int(str(n)[ind])+1)*10**(-ind-1))
                n = n-(int(str(n)[ind])+1)*10**(-ind-1)
                ind-=1
                if n == int("".join(sorted(str(n)))):
                    return n
    print(monotoneIncreasingDigits(332))