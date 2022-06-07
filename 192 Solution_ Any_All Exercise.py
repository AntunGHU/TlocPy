def is_all_strings(lst):
	return all(type(l) == str for l in lst)
	
	
is_all_strings(['a', 'b', 'c'])  #True
is_all_strings([2,'a', 'b', 'c'])  #False
is_all_strings(('hello', 'goodbye'))  #True
