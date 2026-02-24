import requests
import os
import webbrowser as wb

url = "https://alwaysjudgeabookbyitscover.com/"
response = requests.get(url)

with open("web.html", "w", encoding= response.encoding) as f:
    f.write(response.text)

file_path = os.path.realpath("web.html")
print(file_path)
wb.open("file://" + file_path)