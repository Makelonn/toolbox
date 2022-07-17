from pathlib import Path

p = Path("./src")

list_files = list(p.glob("**/*.*"))

ext_list = set()
for f in list_files :
    ext_list.add(f.suffix)

print("List of extension in the folder " + str(p) + ":")
print(ext_list)