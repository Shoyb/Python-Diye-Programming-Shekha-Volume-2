import requests

url = "https://web.archive.org/web/20230331200714/http://dimik.pub/"
response = requests.get(url)
print(response.text)