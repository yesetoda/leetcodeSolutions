class Solution:
    def reverseBits(n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2) 
    print(reverseBits(0b00000000010100101000001111010011100))