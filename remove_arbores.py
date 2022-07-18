from pathlib import Path
import shutil
import sys
from loading_bar import LoadingBar



def remove_arborescence(path_src, path_dest, keep_old=False):
    src = Path(path_src)
    dst = Path(path_dest)

    assert(src.exists())

    # Copy all file from src to dst without the arborture of the folder
    f_list = list(src.glob('**/*.*'))
    print("Total files:", len(f_list))
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
            if keep_old	:
                shutil.copy2(f, dst.joinpath(name))
            else : 
                f.rename(Path(dst, name))
        except Exception as e:
            print(e)
            loader.print_bar()
            # Save path of the file that failed to copy
            with open("failed_files.txt", "a") as failed:
                failed.write(str(f) + "\n")
            continue
        loader.update()
    loader.finish()

remove_arborescence("./unsorted", "./test")