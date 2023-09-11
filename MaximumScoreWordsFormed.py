class Solution:
    def maxScoreWords(words: list[str], letters: list[str], score: list[int]) -> int:
        letter_val = {}
        out = 0
        for i in set(letters):
            letter_val[i] = score[ord(i)-97]
        for h in range(len(words)):
            s = letters[:]
            print(words[h:]+words[:h],letters)
            result = 0
            for i in words[h:]+words[:h]:
                for j in i:
                    print(j,s)
                    if j not in letter_val:
                        result = 0
                        print("not in letter_val")
                        break
                    else:
                        if j in s:
                            result+=letter_val[j]
                            s.remove(j)
                        else:
                            result = 0
                            print("letter not in s")
                            break
                if out<result:
                    out = result
                print(i,result)
        return out
    words = ["hello", "world"]
    letters = ["h", "e", "e", "l", "l", "o", "w", "o", "r", "l", "d"]
    score = [1, 2, 3, 4, 5, 6, 7, 8, 9,9,1,2,3,2,4,2,4,2,2,2,3,2,3,2,2,3]
    print(maxScoreWords(words , letters, score ))
    
