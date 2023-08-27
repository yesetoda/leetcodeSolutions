class Solution:
    def makeSmallestPalindrome(s: str) -> str:
        s = [i for i in s]
        st = 0
        end = len(s)-1
        for i in range(end//2+1):
            if s[st] == s[end]:
                st+=1
                end-=1
            else:
                mn =  min(s[st],s[end])
                s[st] =mn
                s[end] = mn
                st+=1
                end-=1
        return ''.join(s)
    print(makeSmallestPalindrome(s =  "seven"))
        # s = [i for i in s]
        # st = 0
        # en = len(s) - 1  
        # opCount = 0
        # while st < en:
        #     if s[st] != s[en]:
        #         s[st] = s[en]
        #         st += 1
        #         en -= 1
        #         opCount += 1
        #     else:
        #         st += 1
        #         en -= 1
        # return "".join(s)