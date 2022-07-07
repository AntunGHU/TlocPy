# 13'51''
# -url -request/response cycle -header -categories of response -GET&POST request 
# Internet-url: 1)DNS Lookup 2)REQUEST to server 3)Server process request 4)Server issuess a RESPONSE !!! 2-4 cine Request/Response cycle
# DNS Lookup: DNS Server (kao Phonebook interneta)  preuzima "google.com" i pretvara ga u IP broj! 172.217.9.142
# Colt na WebStarnici: View, Source, gomila HTML-coda
# Colt: ^+J pa Network pa prikaz HTTP requestova Name, www.google.com i u centralnom djelu na kartici "Headers" imamo "General" sa url, GET a na kartici "Responses" sav HTML kod
# HTTP Headers: šalju se i uz req i uz res kao dodatne info o njima
    #Npr:    Req Header:-Accept(html, json, xml), -Cache_Ctrl, -User(agent koji šalje)
    #        Res Header:-Access_Ctrl_Allow_Origin, -Allowed(verbs allowed in request)
# ResponseStatusCode: -2xx(Success), -3xx(Redirect), -4xx(Clienterror), -5xx(Servererror)