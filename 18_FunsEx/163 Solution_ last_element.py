def last_element(l):
    try:
        return l[-1]
    except IndexError as e:
        return None
        
last_element([1,2,3]) # 3
last_element([]) # None
