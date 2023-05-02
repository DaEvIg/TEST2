def merge(dic_1, dic_2):
    dic_3 = dic1.copy()
    dic_3.update(dic_2)
    return dic_3


dic1 = {1: "My", 2: "name"}
dic2 = {3: "is", 4: "Danil"}
print(merge(dic1, dic2))
