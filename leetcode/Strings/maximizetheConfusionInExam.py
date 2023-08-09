from collections import Counter

class Solution:
    def maxConsecutiveAnswers(answerKey: str, k: int) -> int:
        maxConsecutive = 0
        left = 0
        right = 0
        changesLeft = k
        maxCount = 0
        counts = {'T': 0, 'F': 0}

        while right < len(answerKey):
            if answerKey[right] != answerKey[right - 1]:
                while changesLeft < 0:
                    counts[answerKey[left]] -= 1
                    left += 1
                    changesLeft += 1

                changesLeft -= (right - left) - 1

            counts[answerKey[right]] += 1
            maxCount = max(maxCount, counts[answerKey[right]])

            currentConsecutive = right - left + 1
            maxConsecutive = max(maxConsecutive, currentConsecutive)

            right += 1

        return maxConsecutive
    print(maxConsecutiveAnswers( answerKey = "TTFTTFTT", k = 1))