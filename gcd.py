def gcd(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a

# Example usage:
result = gcd(24, 36)
print(result)  # Output: 12