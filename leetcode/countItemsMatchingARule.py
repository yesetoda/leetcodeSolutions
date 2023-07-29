class Solution:
    def countMatches(items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            ind = 0
        elif ruleKey =="color":
            ind = 1
        elif ruleKey == "name":
            ind = 2
        out = 0
        for i in items:
            print( ruleValue ,items[items.index(i)][ind])
            if ruleValue == items[items.index(i)][ind]:
                out+=1
        return out
    print(countMatches(items =[["ii","iiiiiii","ii"],["iiiiiii","iiiiiii","ii"],["ii","iiiiiii","iiiiiii"]],ruleKey ="color",ruleValue ="ii"))