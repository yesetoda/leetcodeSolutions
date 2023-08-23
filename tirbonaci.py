
def memorize1(func):
        cache = {}#if the computation is done and not in dict insert it else retrieve the result and pass
        @wraps(func)
        def wrapper(*args, **kwargs):
            key  = str(args) + str(kwargs)
            if key not in cache:
                cache[key] = func(*args, **kwargs)
            return cache[key]
        return wrapper

class Solution:
    @memorize1  #if this is mentioned it will use memozation
    def tribonacci( n: int) -> int:
            fb = [0,1,1,2,4]
            if n<5:
                return fb[n]
            return tribonacci(n-1)+ tribonacci(n-2)+tribonacci(n-3)
                