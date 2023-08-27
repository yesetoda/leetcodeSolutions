l = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,]]
rowmax = [max(i) for i in l]
colmax = []
for i in range(len(l)):
    colmax.append(max([l[j][i] for j  in range(len(l))]))
print(rowmax,colmax)
out = 0
for r in range(len(l)):
    for c in range(len(l)):
        out+=min(rowmax[r],colmax[c])- l[r][c]
print(out)
        