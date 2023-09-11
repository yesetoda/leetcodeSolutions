class Solution:
    def maximumScore( a: int, b: int, c: int) -> int:
        st = sorted([a,b,c])
        count = 0
        while st[1]>0:
            st[1]-=1
            st[2]-=1
            count+=1
            st.sort()
        return count
    def maximumScore2(a: int, b: int, c: int) -> int:
       return min((a+b+c)//2,a+b+c-max(a,b,c))
    print(maximumScore(a = 14095, b =23554, c = 8235))
    print(maximumScore2(a = 14095, b =23554, c = 8235))
