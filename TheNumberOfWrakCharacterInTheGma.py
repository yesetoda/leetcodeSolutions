class Solution:
    def numberOfWeakCharacters(properties: list[list[int]]) -> int:
        at = []
        df = []
        weaks =0
        for i in properties:
            at.append(i[0])
            df.append(i[1])
        for i in range(len(at)-1):
            if at[i] < min(at[:i],at[i+1:]) and df[i] < min(df[:i],df[i+1:]):
                weaks+=1
        return weaks
    print(numberOfWeakCharacters(properties =[[1,5],[10,4],[4,3]]))