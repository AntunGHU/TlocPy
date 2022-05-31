import re
def parse_bytes(input):
	binary_regex = re.compile(r'\b[10]{8}\b')
	results = binary_regex.findall(input)
	return results
	
parse_bytes("11010101 101 323")    # ['11010101']
parse_bytes("my data is: 10101010 11100010")    # ['10101010', '11100010']
parse_bytes("asdsa")   # []
