class Solution:
    def distributeCandies( candies: int, num_people: int) -> list[int]:
        inc = 1
        out = [0 for i in range(num_people)]
        while True:
            for i in range(num_people):
                if candies-inc<=0:
                    out[i]+=candies
                    return out
                out[i]+=inc
                candies-=inc
                inc+=1
        return out
    print(distributeCandies(candies = 127, num_people = 4))
                