from bs4 import BeautifulSoup
# import requests

# http = requests.get("http://radicaltechnologies.co.in/")
# http_doc = http.text
# open("radical_page.html", "w").write(http.text)

http_doc = open("radical_page.html", "r").read()
soup = BeautifulSoup(http_doc, "html.parser")
divs = soup.find_all("div")
courses = []
for div in divs:
    if ('id' in div.attrs) and div['id'] == 'primary':
        li_tags = div.find_all("li")
        for li in li_tags:
            if ('class' in li.attrs) and ('menu-item' in li['class']) and li.string:
                courses.append(li.string)
# to remove duplicates
courses = list(set(courses))
courses.sort()

print("\n".join(courses))