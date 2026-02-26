import io

try:
    with open("lines.txt", "r") as fp:
        content = fp.read()
        fp.write(content)
except FileNotFoundError:
    print("The file line.txt does not exist.")
except IOError:
    print("An error occurred while trying to read the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")