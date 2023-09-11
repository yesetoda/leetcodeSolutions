class Solution:
    def decrypt(code: list[int], k: int) -> list[int]:
        out = []
        leng = len(code)
        if k==0:
            return [0]*leng
        if k>0:
            for i in range(leng):
                if i+1+k<=leng:
                    out.append(sum(code[i+1:i+k+1]))
                else:
                    x = (i+k)-leng
                    out.append(sum(code[i+1:]+code[:x+1]))
        elif k<0:
            code = code[::-1]
            k = -k
            for i in range(leng):
                if i+1+k<=leng:
                    out.append(sum(code[i+1:i+k+1]))
                else:
                    x = (i+k)-leng
                    out.append(sum(code[i+1:]+code[:x+1]))
            out = out[::-1]
        return out
    print(decrypt( code = [5,7,1,4], k = 3 ))
