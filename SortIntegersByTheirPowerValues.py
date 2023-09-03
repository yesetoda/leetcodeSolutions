def srt(lo, hi, k):
    def power_value(x):
        steps = 0
        while x != 1:
            if x % 2 == 0:
                x //= 2
            else:
                x = x * 3 + 1
            steps += 1
        return steps

    lst = [i for i in range(lo, hi + 1)]
    lst.sort(key=lambda x: (power_value(x), x))
    return lst[k-1]

print(srt(lo = 7, hi = 11, k = 4))