from pathlib import Path
import shutil
import sys
from loading_bar import LoadingBar

src = Path('./src')
dst = Path('./dest')

# Copy all file from src to dst without the arborture of the folder
f_list = list(src.glob('**/*.*'))
print("Total files:", len(f_list))
cpt = 0

# Create dst if it doesn't exist
if not dst.exists():
    dst.mkdir()

loader = LoadingBar(len(f_list))

for f in f_list:
    try :
        # Check if the file already exists in dst
        #Add a number to the name of the file
        name = f.name
        number = 1
        while dst.joinpath(name).exists():
            name = str(f.name.split(".")[0] + "_" + str(number) + "." + f.name.split(".")[1])
            number += 1
        # Copy the file
        shutil.copy2(f, dst.joinpath(name))
    except Exception as e:
        print(e)
        loader.renew()
        # Save path of the file that failed to copy
        with open("failed_files.txt", "a") as failed:
            failed.write(str(f) + "\n")
        continue
    loader.update()
print("\nDone.")