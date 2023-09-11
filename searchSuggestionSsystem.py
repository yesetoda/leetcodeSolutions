class Solution:
    def suggestedProducts( products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()
        out = []
        for i in range(len(searchWord)):
            sug = []
            for j in products:
                if j.startswith(searchWord[:i+1]) and len(sug)<3:
                    sug.append(j)
                elif len(sug)>3:
                    break
            out.append(sug)
        return out
    print(suggestedProducts(products =
["mobile","mouse","moneypot","monitor","mousepad"],searchWord ="mouse"))
        
                