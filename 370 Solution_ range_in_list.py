def range_in_list(lst, start=0, end=None):
    end = end or lst[-1]
    return sum(lst[start:end+1])
    
range_in_list([1,2,3,4],0,2) #  6
range_in_list([1,2,3,4],0,3) # 10
range_in_list([1,2,3,4],1) #  9
range_in_list([1,2,3,4]) # 10
range_in_list([1,2,3,4],0,100) # 10
range_in_list([],0,1) # 0
