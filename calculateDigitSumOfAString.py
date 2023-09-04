def dSum( s: str, k: int) -> str:
        rg = 0 if len(s)%k==0 else k-len(s)%k
        for i in range(rg):
            s+="0" 
        print(s)
        news = ""
        for i in range(0,len(s),k):
            sm = 0
            for ch in s[i:i+k]:
                sm+=int(ch)
            print(s[i:i+k],sm)
            news+=str(sm)
        return news if len(news)<=k else digitSum(news,k)
print(digitSum(s = "0000000000000000", k = 3))
        
            