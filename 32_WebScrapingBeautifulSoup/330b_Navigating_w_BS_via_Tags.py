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
data = soup.body.contents[1]
# daje samo div kao 2.el u listi ['\n',<h3..., '\n'] -dobijemo sve unutar <body> taga ali u formatu liste sa puno \n-ova
print(data)
data = soup.body.contents[1].contents
print(data)
data = soup.body.contents[1].next_sibling
print(data)
data = soup.body.contents[1].next_sibling.next_sibling
print(data)
# sad to pokazuje preko parent, find se uzima radi pocetne tocke prema parentu!
data = soup.find(class_="super-special").parent.parent
print(data)
