#

# import regex module
import re

# define our phone number regex
pattern = re.compile(r'\d{3} \d{3}-\d{4}')

# search a string with our regex
res = pattern.search('Call me at 415 555-4242!')
