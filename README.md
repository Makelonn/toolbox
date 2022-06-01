# Toolbox

Some scripts and programs to use in everyday life.

## Picture sort

🔩 How does that work ?

This script will sort all picture in repertory `path_to_picture` depending on the name of the picture. Names should be of the format : `IMG_YEARMONTHDAY_NUMBER`; for example : `IMG_20200521_16` is a picture taken on 21/05/2020. 

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

    python picture_sort.py "path_to_picture"

