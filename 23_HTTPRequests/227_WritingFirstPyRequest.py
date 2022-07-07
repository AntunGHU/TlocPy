# 7'28''
# requests modul, instalira se s:
#? python3.x -m pip3.x install requests
#? python3
#? >>> import requests
#? >>>res=requests.get("https://news.ycombinator.com/")
#? >>>res   #<Response [200]>
#? >>>res.ok   # True
#? >>>res.headers   # {'Date':'Fri', 22Dec...}
#? >>>res.text   # Gomila html-a za human-prikaz
#? >>>quit
# stvarnja fajla
#? touch first_request.py
import requests
# res=requests.get("http://www.google.com/")
# url1="://www.google.com"                  # bez http
# url2="http://www.google.com/blablabla"    # sa /blablabla
url="http://www.google.com"
# res=requests.get(url1)    # Your request to http... 404
# res=requests.get(url2)    # Your request to http... 404
res=requests.get(url)       # Your request to http... 200
print(f"Your request to {url} came back with status code {res.status_code}")

