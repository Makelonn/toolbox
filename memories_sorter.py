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

def memories_sorter(src, dest):
    pass

a = "NAME_20010217_16301254.jpg"
print(image_name_parser(a))
print(monthly_str(image_name_parser(a)["info_time"]["month"]))

current_repository = Path('./unsorted')
aim_repository = Path('./sorted')

d1 = mpimg.imread(Path(current_repository, "1.jpg"))
d2 = mpimg.imread(Path(current_repository,"3.jpeg"))

image_plotting(d1,d2)