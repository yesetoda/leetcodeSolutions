class Solution:
    def kWeakestRows( mat: list[list[int]], k: int) -> list[int]:
        freq = {}
        for i in range(len(mat)):
            freq[i] = mat[i].count(1)
        sorted_rows = sorted(freq.items(), key=lambda x: x[1])
        print(sorted_rows)
        return [row[0] for row in sorted_rows[:k]]
    print(kWeakestRows( mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], k = 3))