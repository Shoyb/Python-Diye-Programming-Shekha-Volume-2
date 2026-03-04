import re

text = "book at subeen.com, book At subeen.com, book (at) subeen dot com, book [at] subeen [dot] com"
text = re.sub(r'\s+[\(\[]*\s*at\s*[\)\]]*\s+', '@', text, flags=re.I)
text = re.sub(r'\s+[\(\[]*\s*dot\s*[\)\]]*\s+', '.', text, flags=re.I)
print(text)