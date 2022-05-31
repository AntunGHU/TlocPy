import re 

def is_valid_time(input):
    pattern = re.compile(r'^\d\d?:\d\d$')
    mo = pattern.search(input)
    if mo:
        return True
    return False
    
is_valid_time("10:45")       #True
is_valid_time("1:23")        #True
is_valid_time("10.45")       #False
is_valid_time("1999")        #False
is_valid_time("145:23")      #False
# In order to return True, the string should ONLY contain the time, and no other characters
is_valid_time("it is 12:15") #False
is_valid_time("12:15")       #True
# Don't worry about impossible times like 88:76, just focus on the formatting!
is_valid_time("34:55") #True
