from bs4 import BeautifulSoup
import requests

http = requests.get("https://www.dishtv.in/Pages/channel-number-list.aspx")
http_doc = http.text
open("dishtv_channels.html", "w").write(http.text)

http_doc = open("dishtv_channels.html", "r").read()
soup = BeautifulSoup(http_doc, "html.parser")

channels = {}

table = soup.find("table")
for row in table.find_all('tr'):
    data = [x.string.strip() for x in row.find_all('td') if x and x.string]
    print(data)
    try:
        channels[int(data[-1])] = data[0]
    except IndexError:
        # cames for the first table row, for which there is no td, just has th
        pass

for channel_number in sorted(channels.keys()):
    print(channel_number, channels[channel_number])
