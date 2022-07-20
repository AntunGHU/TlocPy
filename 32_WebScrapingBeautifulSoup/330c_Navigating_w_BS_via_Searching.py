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
data = soup.find(id="first").find_next_sibling()
print(data)  # [<ol><li..]
data = soup.find(id="first").find_next_sibling().find_next_sibling()
print(data)  # <div..
data = soup.select("[data-example]")[1].find_previous_sibling()
print(data)  # ide unazad
# u metod-zagradu moze se staviti i argument, npr ath(class_="special")
data = soup.find("h3").find_parent()
print(data)  # i skace level vise! <div...

# Za kraj Ath pokazuje sa "help(data)" koliko dundera imamo i kolko je veliki help. Kaze: Kad god radi scraping uvijek koristi dokumentaciju svakog modula kojeg koristi. Za "one-time" use previse bi to bilo, i nepotrebno, sve zapamtiti.
print(help(data))
