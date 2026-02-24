import requests

url = "http://web-scraping.dev/api/download-file"
response = requests.post(
    url,
    headers={"Content-Type": "application/x-www-form-urlencoded"}
)
if response.ok is False:
    print("Error downloading the file")

with open("book.pdf", "wb") as f:
    f.write(response.content)

print("Book download completed.")