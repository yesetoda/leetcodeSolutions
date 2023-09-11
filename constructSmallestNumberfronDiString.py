class Solution:
    def smallestNumber(pattern: str) -> str:
        stack = []
        ans = []

        for i in range(len(pattern) + 1):
            stack.append(i + 1)
            print(stack)
            if i == len(pattern) or pattern[i] == 'I':
                print("i==>",i,"pattern==>",pattern[i] if i<len(pattern) else None)
                while stack:
                    ans.append(str(stack.pop()))
                    print("stack==>",stack,"ans==>",ans)


        return ''.join(ans)
    print(smallestNumber(pattern="IDDD"))