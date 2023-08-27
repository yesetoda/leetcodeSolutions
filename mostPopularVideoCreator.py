class Solution:
    def mostPopularCreator(creators: list[str], ids: list[str], views: list[int]) -> list[list[str]]:
        c = []
        id = [[] for i in range(len(creators))]
        v = [0  for i in range(len(creators))]
        for i in range(len(creators)):
            if creators[i] not in c:
                c.append(creators[i])
                id[c.index(creators[i])].append(f"{views[i]}{ids[i]}")
                v[c.index(creators[i])]+=views[i]
            else:
                id[c.index(creators[i])].append(f"{views[i]}{ids[i]}")
                v[c.index(creators[i])]+=views[i]
        print(c)
        print(id)
        print(v)                
                
            
        
        # # creator_id_view = {}
        # # for i in range(len(creators)):
        # #     if creators[i] not in creator_id_view:
        # #         creator_id_view[creators[i]]= [[(ids[i],views[i])],views[i]]
        # #     else:
        # #         creator_id_view[creators[i]][0].append((ids[i],views[i]))
        # #         creator_id_view[creators[i]][1]+=views[i]
        # # fin = creator_id_view.sort(key= lambda x: creator_id_view[x][1])
        # # print(fin)
        # # return creator_id_view
        
        # creator_id_view = {}
        # for i in range(len(creators)):
        #     if creators[i] not in creator_id_view:
        #         creator_id_view[creators[i]] = [[(ids[i], views[i])], views[i]]
        #     else:
        #         creator_id_view[creators[i]][0].append((ids[i], views[i]))
        #         creator_id_view[creators[i]][1] += views[i]
        # sorted_creators = sorted(creator_id_view.items(), key=lambda x: x[1][1], reverse=True)
        # return sorted_creators
    print(mostPopularCreator( creators = ["alice","bob","amy","alie"], ids = ["one","two","three","four"], views = [5,10,5,4]))