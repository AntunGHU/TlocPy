# I've given you a list called sounds .  It looks like # this: sounds = ["super", "cali", "fragil", "istic", # "expi", "ali", "docious"] 
# Write code that loops over the list and adds all the # strings together to form one large combined string # (don't add any spaces between them) 
# The combined string should be in all UPPERCASE as well 
# Save the result in a variable called result  

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
result = ''

for s in sounds:
    result += s
result = result.upper()
