dict1 = {'Nikhil': {'English': 5, 'Maths': 2, 'Science': 14},
         'Akash': {'English': 15, 'Maths': 7, 'Science': 2},
         'Akshat': {'English': 5, 'Maths': 50, 'Science': 20}}
def asc(dic):
    dict2 = {}
    for key, val in dic.items():
        dict3 = {}
        sort_val = dict(sorted(val.items(), key=lambda item: item[1], reverse=False))
        dict3.update(sort_val)
        dict2.update({key: dict3})
    return dict2
print(asc(dict1))