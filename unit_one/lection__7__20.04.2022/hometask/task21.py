# Задан словарь, его значения необходимо внести по соответвющим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}


template = """ 
<!DOCTYPE HTML>
<html>
 <head>
  <title> ? </title>
  <meta charset=?>
 </head>
 <body onload="alert(?)">
 
  <p>?</p>

 </body>
</html>
"""

list_html = []
index = []
f = open("index.html", "w+", encoding="UTF-8")
f.writelines(template)

f = open("index.html", "r+t", encoding="UTF-8")

list_html = f.readlines()

for key, val in page.items():
        for i in list_html:
                if key in i:
                        x = list_html.index(i)
                        i = i.replace("?", val)
                        list_html[x] = i

f.seek(0,0)
f.writelines(list_html)

f.close()