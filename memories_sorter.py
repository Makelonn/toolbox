"""This files helps you to sort by year/month all images from a repository to another"""

from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path


def image_name_parser(filename):
    # Format : IMG_YYYYMMDD_HHMMSSSS.ext
    f_split = filename.split("_")
    ext = f_split[-1].split(".")
    f_split = f_split[:-1] + ext
    info ={
        "info_time" : {
            "year": f_split[1][0:4],
            "month": f_split[1][4:6],
            "day": f_split[1][6:8],
            "hour": f_split[2][0:2],
            "min": f_split[2][2:4],
            "sec": f_split[2][4:6]
        },
        "info_else" : {
            "name":f_split[0],
            "ext": f_split[-1]
        }
    }
    return info

def monthly_str(month_number):
    translator = {
        "01":"January",
        "02":"February",
        "03":"March",
        "04":"April",
        "05":"May",
        "06":"June",
        "07":"July",
        "08":"August",
        "09":"September",
        "10":"October",
        "11":"November",
        "12":"December"
    }
    return translator[month_number]

def image_plotting(img1, img2):
    plt.subplot(1, 2, 1)
    plt.axis('off')
    plt.imshow(img1)
    plt.subplot(1, 2, 2)
    plt.imshow(img2)
    plt.axis('off')
    plt.show()

def read_img(img_name, srcfolder):
    p = Path(srcfolder, img_name)
    return mpimg.imread(p)

def list_files(folder):
    return list(folder.glob("**/*.*"))

def memories_sorter(src, dest):
    file_list = list_files(src)
    for mem in file_list:
        name = mem.parts[-1]
        print(image_name_parser(name))
    pass


current_repository = Path('./unsorted')
aim_repository = Path('./sorted')

memories_sorter(current_repository, aim_repository)