from collections import Counter
class Solution:
    def furthestDistanceFromOrigin( moves: str) -> int:
        chk = set(moves)
        freq = sorted(list(Counter(moves).values()),reverse = True)
        return sum(freq)-2*freq[-1] if "R" in chk and "L" in chk else sum(freq) 
        
    print(furthestDistanceFromOrigin(moves = "_R__LL_"))
        
        
        
        