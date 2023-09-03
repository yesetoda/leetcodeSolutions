class Solution:
    def countBinarySubstrings( s: str) -> int:
        count = 0
        leng =len(s)
        for i in range(leng-1):
            for j in range(leng,i+1,-1):
                news =  s[i:j]
                if news.count("1")== news.count("0"):
                    if "0"*(len(news)//2) in news and "1"*(len(news)//2) in news:
                        count+=1
                        print(news,count)
        return count
    print(countBinarySubstrings(s = "00110011"))

        