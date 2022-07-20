# 6'45

# Accessing Data in Elements
# ? get_text - access the inner text in an element
# ? name - tag name
# ? attrs - dictionary of attributes
# ? You can also access attribute values using brackets!

from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

el = soup.select(".special")[0]
print(el.get_text())  # stvarni text
print(el)

for el in soup.select(".special"):
    print(el.get_text())

# Ako oznaku klase 'class="special"' stavimo u HTML liniju koja nema texta, gornja for-petlja vraca praznu liniju na izlat!!! a ne gresku!!!
# zamjena u petlji sa "el.name"
for el in soup.select(".special"):
    print(el.name)  # dobili imena
    print(el.attrs)

# U gornjoj petlji i dict-prikazu "attrs"-a, nasuprot 'class' je lista ['special']. Ona ce imati jos elemenata (odvojenih zarezima, npr ["special", "super-special"]) ako smo pri navodjenju atributa u HTML dodali jos jedan odvojen whitespace-om npr kao u <ol> <li class="special supe-special">This is special</li>
# Nalazenje attributa tj vrijednosti iza oznaka "=", sa find
# trazenje ="Yes"-a nasuprot attributa "data-example" unutar <h3>
attr = soup.find("h3")["data-example"]
print(attr)  # Yes i zaista nam isporucuje vrijednost iza tj "yes", ili
attr = soup.find("div")["id"]  # trazenje u redu <div id="first">
print(attr)  # first !!!radi!!!
# To sto smo oznacvili unutar zagrada [] mozemo dobiti i ako ga zamjenimo s "attrs"
attr = soup.find("div").attrs  # i daje nam sve atribute u div-u
