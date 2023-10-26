html_file = """
<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>
   Ilk Web sitesi
  </title>
 </head>
 <body>
  <h1>
   Ilk Web Sitesi Tasarimi
  </h1>
  <div class="Group 1">
   <h2>
    Ana Sayfa
   </h2>
   <ul>
    <li>
     Menu 1
    </li>
    <li>
     Menu 2
    </li>
    <li>
     Menu 3
    </li>
   </ul>
  </div>
  <div class="Group 2">
   <h2>
    Hakkinda
   </h2>
   <ul>
    <li>
     Menu 1
    </li>
    <li>
     Menu 2
    </li>
    <li>
     Menu 3
    </li>
   </ul>
  </div>
  <img alt="" src="first.jpg"/>
 </body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_file, 'html.parser')

result = soup.prettify()
result = soup.title.name
result = soup.head.title
result = soup.body
result = soup.title.string
result = soup.findAll('h1')

print(result)