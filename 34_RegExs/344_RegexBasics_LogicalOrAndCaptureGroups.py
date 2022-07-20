# 10'28

# * LOGICAL OR
# ?     | (pipe character): "Mr|Mrs|Ms"
# odnosi se na sve s obe strane osim ako ga ne ogranicimo zagradama () ali bez \(\).

# todo Biljezenje:
# \(\d{3}\)|\d{3} = 425 ali i = (425)   - zagrade nemaju zagradnu-grupirajucu ulogu u RE nego doslovnu
# (\(\d{3}\)|\d{3}) \d{3} \d{4} = 415 345 1234 ali i = (415) 345 1234
# Mr. = Mr. = Mrs. (jer je "." oznaka za sve sto ide uz Mr) ali Mr\. je samo Mr.
# (Mr\.|Mrs\.)(([A-Za-z]+) ([A-Za-z]+)) = Mr.(Mrs.) Luca(Tilda) Guardioli(Switon) Ako trebamo nase znakove čćš itd, dopisemo ih u [] posebno
# Zagrade bez \ sluze za formiranje "Match-grupa" poklapanja sto je znacajno za konverziju u Py-u.
# Jos jedan primjer sa Web-adresom:
# ? (https?://)([A-Za-z_-]+\.[A-Za-z]+) = https://pytex.org ali i http://google.com
