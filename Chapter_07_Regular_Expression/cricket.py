import re

with open("cricketer.html", "r") as f:
    s = f.read()
r = re.findall(r'<li>\n(.*?)\n\s+<ol>\n\s+<li>(.*?)</li>\n\s+<li>(.*?)</li>\n\s+</ol>', s)

for i in r:
    print(i[0] + ' - ' + i[1] + ', ' + i[2])