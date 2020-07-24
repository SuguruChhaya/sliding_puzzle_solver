row_list = [[1,2,3], [4,5,6], [7,8,9]]
col_list = [[1,4,7], [2,5,8], [3,6,9]]

#*Since I cannot directly 
for list_ in row_list:
    for item in list_:
        if item == 4:
            print(list_.index(item))
            print(row_list.index(list_))