class Solution:
    def arrangeWords( text: str) -> str:
        dicto = {}
        for ind, ch in enumerate(text.split()):
            dicto[ind] = len(ch)
        
        lengs = sorted(dicto.values())
        out = []
        for length in lengs:
            for word, word_length in dicto.items():
                if word_length == length:
                    out.append(text.split()[word])
        x = len(text.split())
        arranged_text = ' '.join(out[:x]).capitalize()
        return arranged_text

    print(arrangeWords(text = "To be or not to be"))