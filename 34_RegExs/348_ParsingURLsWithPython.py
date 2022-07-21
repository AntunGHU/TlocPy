# 9'31

import re
url_regex = re.compile(
    r'(https?)://(www\.[A-Za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
# match = url_regex.search("http://www.youtube.com/videos")
match = url_regex.search("https://www.my-website.com/bio?data=blak&dog=yes")
# http://www.youtube.com/videos  # https://www.my-website.com/bio?data=blak&dog=yes
print(match.group())

# standardni i dosad koristeni nacin pretrage. Ali, sto ako zelimo izvrsiti npr istrazivanje o zastupljenosti pojedinih domena (.com, .org, .info, itd) ili http naspram https itd. Tada bi nam bilo dobro moci pratiti izlaz samo po tim zeljenim stavkama. Do dovodi do tzv "grupiranja" regex-a sa () !!!. U pytex-u dobijamo tzv "Match group-e" sa strane! U py-kodu dodane zagrade nece nista poremetiti a ako umjesto "match.group()" koristimo "match.groups()" dobijamo tuple sa grupnim poklapanjem

# ('http', 'www.youtube.com', '/videos') # ('https', 'www.my-website.com', '/bio?data=blak&dog=yes')
print(match.groups())

# I sa "group()" mi mozemo dobiti rasclanjeni izlaz ako dodamo "arg(0,1,.." ali oni malo odstupaju od Py-logike jer "group(0)=group()" i daje sve a "group(1)" daje "http", group(2) daje "www..."

print(f"Protocol: {match.group(1)}")  # Protocol: http  # Protocol: https
# Domain: www.youtube.com   # Domain: www.my-website.com
print(f"Domain: {match.group(2)}")
# Everything Else: /videos # Everything Else: /bio?data=blak&dog=yes
print(f"Everything Else: {match.group(3)}")

# Radi vjezbe Ath jos testira "https://www.my-website.com/bio?data=blak&dog=yes"
