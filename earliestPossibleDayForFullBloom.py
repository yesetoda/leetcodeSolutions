
def bloomDate(plantTime,BloomTime):
    print(BloomTime)
    days = 0
    bloomdays = sum(BloomTime)
    for i in range(len(plantTime)):
        print(days,bloomdays)
        days+=plantTime[i]
        bloomdays-=BloomTime[i]
    return days+bloomdays+BloomTime[-1] if len(plantTime)>1 else plantTime[0]+BloomTime[0]
print(bloomDate([i for i in range(1,11)],[i for i in range(10,0,-1)]))
    
    
    
    