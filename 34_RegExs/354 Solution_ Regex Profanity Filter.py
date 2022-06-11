import re

def censor(input):
	pattern = re.compile(r'frack\w*\b', re.IGNORECASE)
	return pattern.sub("CENSORED", input)
	
censor("Frack you")                #"CENSORED you"
censor("I hope you fracking die")  #"I hope you CENSORED die"
censor("you fracking Frack")       #"You CENSORED CENSORED"
