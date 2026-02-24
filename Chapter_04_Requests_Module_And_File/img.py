import requests
import sys

# Test image https://cdn.waifu.im/7236.png

url = sys.argv[1]
name = sys.argv[2]
r = requests.get(url)
with open(name, "wb") as f:
    f.write(r.content)