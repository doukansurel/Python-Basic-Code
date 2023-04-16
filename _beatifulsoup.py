html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlk Web Sayfası</title>
</head>
<body><h1 id="header">
    Pyhton Kursu

</h1>
      <div class="grup1">
         <h2>
            Programlama
         </h2>
            <ul>
                <li>Menü1</li>
                <li>Menü2</li>
                <li>Menü3</li>
            </ul>
</div>
 <div class="grup2">
        <h2>
           Modüller 
        </h2>
           <ul>
               <li>Menü1</li>
               <li>Menü2</li>
               <li>Menü3</li>
           </ul>
</div>
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
</body>
</html>
"""





import re
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,"html.parser")
result = soup.prettify()
result = soup.title
result = soup.div.findChildren()
result = soup.find_all("a")
for i in result:
    print(i.get("href"))
#print(result)




