if __name__ == '__main__':
    N = int(input())
    out = []
    com = [input() for i in range(N)]
    for i in com:
        if "insert" in i:
            out.insert(int(i.split()[1]),int(i.split()[2])) 
        elif "print" in i:
            print(out)
        elif "remove" in i:
            out.pop(out.index(int(i.split()[1])))
        elif "sort" in i:
            out = sorted(out)
        elif "pop" in i:
            out.pop()
        elif "reverse" in i:
            out = sorted(out,reverse=True)
        elif "append" in i:
            out.append(int(i.split()[1]))
    