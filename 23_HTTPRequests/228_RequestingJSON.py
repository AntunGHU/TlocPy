# 11'18
# opca forma requests Headers-a
#! request Headers
#? import requests
#? response = requests.get("http://www.example.com", 
#?      headers= {
#?          "header1":"value1"
#?          "header2":"value2"
#?      }
#? )
# konkretan primjer scripte
#? touch headers.py
import requests
url = "https://icanhazdadjoke.com/"
response= requests.get(url, headers={"Accept":"text/plain"}) # nemaju sci API plain, opcija:"text/html"
print(response.text) # I plain daje 1 recenicu a html gomilu!!!

# osim plain i html mozemo traziti i JSON form podataka
import requests
url = "https://icanhazdadjoke.com/"
response= requests.get(url, headers={"Accept":"application/json"}) 
print(response.text)
print(response.json()) # uzima json i pretvara u Py dictionaru. Bez ovog metoda json() to lici na py-dicz ali je zapravo samo obican text, 
print(response.text)
print(type(response.text)) # <str> koji se mora sa json() pretvoriti u Py-dict. Nakon toga to je dict
data=response.json()
print(type(data))   # <dict>
print(data["joke"]) # "Did you hear..."
print(f"Status:{data['status']}") # 200

