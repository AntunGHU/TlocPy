# QueryString - pass data to server kao dijelove GET requesta
# http://www.example.com/?key1=value1&key2=value2

# QueryString in Py: option1
#? import requests
#? response = requests.get("http://www.example.com/?key1=value1&key2=value2")

# QueryString in Py: option2-preferable zato jer daje vise opcija, mozemo koristiti varijable, dict-e itd a i lakse je nego opcija1
#? import requests
#? response = requests.get(
#?     "http://www.example.com",
#?     params={
#?         "key1":"value1",
#?         "key2":"value2"
#?     }
#? )

# Primjer: Colt cita upute API sucelja ovog site-a! prvo pokazuje u browseru u search baru: "....com/search? term=cat&limit=1"
import requests
url = "http://www.example.com/?key1=value1&key2=value2"
response = requests.get(
    url,
    headers={"Accept":"aplication/json"},
    params={"term":"cat", "limit":1}       # moze biti i varijabla, npr user-input
)
data = response.json()
print(data["results"])          # i dobije se [lista sa {dictima}] sa puno rezultata. Kako bi to ogranicio pokazuje modifikaciju linije "params" tako sto joj dodaje parametar "limit"