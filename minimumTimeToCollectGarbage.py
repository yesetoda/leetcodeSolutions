travel = [2,4,3]
garbage = ["G","P","GP","GG"]
s = {"G":False,"P":False,"M":False}
for i in ["G","P","M"]:
    if i in "".join(garbage):
        s[i] = True
for truck,exist in s.items():
    if exist:
        for i in garbage:
        