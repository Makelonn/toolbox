# Toolbox

Some scripts and programs to use in everyday life.

## Memories sorter

🔩 How does that work ?

This script will sort all picture in repertory `path_to_picture` depending on the name of the picture. Names should be of the format : `IMG_YEARMONTHDAY_HOURMINSEC`; for example : `IMG_20200521_160512` is a picture taken on 21/05/2020. 

Folder structure :

    ├── ...
    ├── path_to_picture                    
    │   ├── 2020
    │   │   ├── jan
    │   │   ├── feb
    │   │   ├── ...
    │   ├── 2021  
    │   └── 20xx                
    └── ...

📚 Usage

    python memories_sorter.py

## Remove arborescence

🔩 How does that work ?

This script will takes every file in the `/src` recursively and copy them in the `/dest` folder. It will add "_number" to the name of the file if the file already exist.

If it fails to copy a file, it will print the error and save the path to a file nammed `failed_files.txt`.

📚 Usage

Edit the `src` and `dest` variables to match the source path and destination path you want. Then use :

    python remove_arbores.py

## Get extension list

🔩 How does that work ?

This simple script allows you to get a list of all extensions existing in the folder you specify, recursively.

📚 Usage

First, you need to edit the path variable to match the path you want to scan. Then use :

    python get_extension_list.py