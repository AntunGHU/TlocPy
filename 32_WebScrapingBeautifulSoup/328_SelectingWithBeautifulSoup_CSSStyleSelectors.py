# 4'03

# trazenje na osnovu CSS-selectora: "select" vraca uvjek "list" of elements matching CSS Selector
# ... select "by id" (of foo npr): #foo
# ... select "by class" (of bar npr): .bar
# ... select of children: div>p
# ... select discendents: div p

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

print(soup.select("#first"))
print(soup.select("#first")[0])
print(soup.select(".special"))
print(soup.select("div"))
print(soup.select("[data-example]"))

# * Komparacija
# Find an element w/ an id of "foo"
soup.find(id="foo")
soup.select("#foo")
# Find all elements w/ class of "bar"-carefull!, "class" is reserved word in Py
soup.find_all(class_="bar")
soup.select(".bar")
# Find all elements w/ data attribute of "baz using general attrs kwarg"
soup.find_all(attrs={"data-buz": "True"})
soup.select("[data-buz]")
