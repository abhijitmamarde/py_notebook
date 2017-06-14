from bs4 import BeautifulSoup
import requests

http = requests.get("http://www.tatasky.com/wps/portal/TataSky/channels/findyourchannel")
http_doc = http.text
open("tatasky_channels.html", "w").write(http.text)

http_doc = open("tatasky_channels.html", "r").read()
soup = BeautifulSoup(http_doc, "html.parser")

channels = {}

table = soup.find("table")
for row in table.find_all('tr'):
    data = [x.string.strip() for x in row.find_all('td')]
    try:
        channels[int(data[-1])] = data[0]
    except ValueError:
        # cames for the first table row, which is heading
        pass

for channel_number in sorted(channels.keys()):
    print(channel_number, channels[channel_number])
