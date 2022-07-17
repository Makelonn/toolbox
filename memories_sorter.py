"""This files helps you to sort by year/month all images from a repository to another"""

from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path
import shutil
from loading_bar import LoadingBar


def image_phone_parser(filename):
    # Format : IMG_YYYYMMDD_HHMMSSSS.ext
    f_split = filename.split("_")
    if len(f_split) < 3:
        return None
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
    if info['info_else']['name'] != "IMG":
        return None
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

def list_files(folder):
    return list(folder.glob("**/*.*"))

def memories_sorter(src, dest, keep_old=False):
    file_list = list_files(src)
    print(len(file_list))
    loader = LoadingBar(len(file_list))
    for mem in file_list:
        name = mem.parts[-1]
        parsed_name = image_phone_parser(name)
        if parsed_name is None:
            continue
        year = parsed_name["info_time"]["year"]
        # Check if the folder year exists in dest
        if not Path(dest, year).exists():
            Path(dest, year).mkdir()
        # Check if the folder month exists in dest/year
        month = monthly_str(parsed_name["info_time"]["month"])
        if not Path(dest, year, month).exists():
            Path(dest, year, month).mkdir()
        # Create the name of the new file
        time_info = parsed_name["info_time"]["hour"] + "h" + parsed_name["info_time"]["min"] + "m" + parsed_name["info_time"]["sec"] + "s"
        new_name = parsed_name["info_else"]["name"] +"_" + parsed_name["info_time"]["day"] + "_" + time_info + "." + parsed_name["info_else"]["ext"]
        # Check if the file already exists in dest/year/month
        number = 1
        while Path(dest, year, month, new_name).exists():
                new_name = parsed_name["info_else"]["name"] + time_info + "_" + str(number) + "." + parsed_name["info_else"]["ext"]
                number += 1
        # Copy the file
        if keep_old :
            shutil.copy2(mem, Path(dest, year, month, new_name))
        else :
            mem.rename(Path(dest, year, month, new_name))
        loader.update()
    loader.finish()

current_repository = Path('/Memories/tmp/jpg/classic_format')
aim_repository = Path('/Memories/Photos')

memories_sorter(current_repository, aim_repository)