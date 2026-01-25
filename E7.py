import os

files = os.listdir(".")
i = 1
for file in files:
    if file.endswith("jpg"):
        os.rename(file, f"{i}.jpg")
        i += 1