def ordered(orders):
    order_types = []
    tab_order = {}
    for i in orders:
        if i[2] not in order_types:
            order_types.append(i[2])
        if i[1] not in tab_order:
            tab_order[i[1]] = {i[2]:1}
        else:
            if i[2] not in tab_order[i[1]]:
                tab_order[i[1]][i[2]] = 1
            else:
                tab_order[i[1]] = {i[2]:int( tab_order[i[1]][i[2]] )+1}
    order_types.sort(key = lambda x:x.split()[0])
    print("\t",*order_types)
    return tab_order,order_types


print(ordered([["david","3","ceriche"],["corina","10","beef borrito"],["david","3"," fried chicken"],["carla","5","water"],["carla","5","ceriche"],["rous","3","ceriche"]]))

# def sq(num):
    