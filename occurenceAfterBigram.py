class Solution:
    def findOcurrences( text: str, first: str, second: str) -> list[str]:
        finder = text.split()
        thirds = []
        wanted = first+" "+second
        for ind,word in enumerate(finder):
            if ind<len(finder)-2:
                print(ind,word,finder[ind+1],finder[ind+2])
                if word==first and finder[ind+1] == second:
                    thirds.append(finder[ind+2])
        return thirds
    print(findOcurrences(text = "alice is a good g", first = "a", second = "good"))

        