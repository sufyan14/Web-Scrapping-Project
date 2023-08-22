import requests
from bs4 import BeautifulSoup

with open("sample.html", "r") as f:
    html_doc = f.read()  # html_doc will now contain the content of sample.html

soup = BeautifulSoup(html_doc, 'html.parser')  # soup object

# print(soup.prettify()) # simply prints it
# print(soup.div.string, type(soup.div.string)) # can print one tag from the file
# print(soup.find_all("div"))

# printing all the links
# for link in soup.find_all("a"):
#     print(link.get("href"))
#     print(link.get_text())

# s = soup.find(id="link3")
# print(s.get("href"))

# print(soup.select("div.italic"))
# print(soup.span.get("class"))

# print(soup.find(id="italic"))
# for child in soup.find(class_="container").children:
#     print(child)

# for parent in soup.find(class_="box").parents:
#     print(parent)
#     break

# cont = soup.find(class_="container") # Change elements in tags
# cont.name = "span"
# cont["class"] = "myclass class2"
# cont.string = "String is heree!"
# print(cont)

# ulTag = soup.new_tag("ul") # Print tags and modify your html

# liTag = soup.new_tag("li")
# liTag.string = "Home"
# ulTag.append(liTag)

# liTag = soup.new_tag("li")
# liTag.string = "Contact"
# ulTag.append(liTag)

# soup.html.body.insert(0, ulTag)
# with open("modified.html", "w") as f:
#     f.write(str(soup))

# cont = soup.find(class_="container")
# print(cont.has_attr("class"))

# def has_class_but_not_id(tag):
#     return tag.has_attr("class") and not tag.has_attr("id")

# results = soup.find_all(has_class_but_not_id)
# print(results)

def has_content(tag):
    return tag.has_attr("content")

results = soup.find_all(has_content)
for result in results:
    print(result, "\n")

    

