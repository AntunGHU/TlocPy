# 6'43''
# ima ju svaki py-fajl, ako je fajl glavni onda je njena vrijednost "__main__"
# morao kreirati samostojece fajlove say-hi i say-sup koji samostalno pokrenuti imaju vrijednost __main__
# medjutim kad sam say_hi nadogradio importanjem say-sup-a, say_hi i dalje ima __main__ ali say_sup vise nema __main__ nego __say_sup__ te se je dvaput izvodio, jedanput kad se importao i drugi put kad je pozivan. 
# Kako bi se to sprijecilo stavljamo kondicional if u say_sup