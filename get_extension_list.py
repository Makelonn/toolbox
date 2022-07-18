from pathlib import Path


def get_extension_list(path_to_folder='.'):
    path_to_folder = Path(path_to_folder)

    list_files = list(path_to_folder.glob("**/*.*"))

    ext_list = set()
    for f in list_files :
        ext_list.add(f.suffix)

    print("List of extension in the folder " + str(path_to_folder) + ":")
    print(ext_list)
