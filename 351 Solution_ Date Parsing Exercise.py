import re

def parse_date(input):
	pattern = re.compile("^(\d\d)[,/.](\d\d)[,/.](\d{4})$")
	match = pattern.search(input)
	if match:
		return {
			"d": match.group(1),
			"m": match.group(2),
			"y": match.group(3),
		}
	return None
	
parse_date("12,04,2003")  #{'d': '12', 'm': '04', 'y': '2003'}
parse_date("12.11.2003")  #{'d': '12', 'm': '11', 'y': '2003'}
parse_date("12.11.200312") #None
