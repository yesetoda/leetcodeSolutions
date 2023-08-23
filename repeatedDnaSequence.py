class Solution:
    def findRepeatedDnaSequences( s: str) -> list[str]:
        # st = 0
        # freq = {}
        # for i in range(10,len(s)+1):
        #     print(s[st:i])
        #     if s.count(s[st:i])>=1:
        #         if s[st:i] not in freq.keys():
        #             freq[s[st:i]]  = 1
        #         else:
        #             freq[s[st:i]] +=1 
        #     st+=1
        # return [ i for i in freq.keys() if freq[i]>1]
        
        if len(s) < 10:
            return []
        sequences = set()
        repeated_sequences = set()
        for i in range(len(s) - 9):
            sequence = s[i:i+10]
            if sequence in sequences:
                repeated_sequences.add(sequence)
            else:
                sequences.add(sequence)
        return list(repeated_sequences)
    print(findRepeatedDnaSequences(s ="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))