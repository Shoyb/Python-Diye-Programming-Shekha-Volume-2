content = []
with open("countries.txt", "r") as fp:
    content = fp.readlines()

character = [chr(i) for i in range(ord("a"), ord("z") + 1)]
for i in character:
    for j in content:
        if j.lower().startswith(i):
            with open(f"{i}.txt", "a") as f:
                f.write(j)