"""This files helps you to sort by year/month all images from a repository to another"""

from pathlib import Path
import shutil
from loading_bar import LoadingBar


def format_phone_parser(filename):
    """
    It takes a filename as input, and returns a dictionary with the following keys:
    
    - info_time: a dictionary with keys year, month, day, hour, min and sec
    - info_else: a dictionary with keys name, end and ext
    - new_name: a string with the new name of the file
    
    The function is designed to work with filenames that follow the format:
    
    `IMG_YEARMMDD_HHMMSSSS.ext`
    
    where YEAR is a 4 digit year, MM is a 2 digit month, DD is a 2 digit day,
    HH is a 2 digit hour, MM is a 2 digits minute, SSSS is the seconds, 
    and ext is an extension
    
    :param filename: The name of the file you want to parse
    :return: A dictionary with the following keys: info_time, info_else, new_name
    """
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
            "end" : "".join(f_split[3:-1]),
            "ext": f_split[-1]
        },
        "new_name": f_split[0]+"_"+f_split[1][6:8]+"_"+f_split[2][0:2]+"h"+f_split[2][2:4]+"m"+f_split[2][4:6]+"s"+"".join(["_" if len(f_split[3:-1])>0 else ""]+f_split[3:-1])
    }
    # New name = IMG_DD_HHMMSSSS_END.ext
    return info

def format_wa_parser(filename):
    """
    It takes a filename as input, and returns a dictionary with the following keys:
    
    - info_time: a dictionary with keys year, month, and day
    - info_else: a dictionary with keys name and ext
    - new_name: a string with the new name of the file
    
    The function is designed to work with filenames that follow the format:
    
    `IMG-YEARMMDD-WAXXXX.ext`
    
    where YEAR is a 4 digit year, MM is a 2 digit month, DD is a 2 digit day, WA is a string of 4
    characters, and ext is an extension
    
    :param filename: The name of the file you want to parse
    :return: A dictionary with the following keys:
    """
    # Format : IMG-YEARMMDD-WAXXXX.ext
    f_split = filename.split("-")
    if len(f_split) < 3:
        return None
    ext = f_split[-1].split(".")
    f_split = f_split[:-1] + ext
    info ={
        "info_time" : {
            "year": f_split[1][0:4],
            "month": f_split[1][4:6],
            "day": f_split[1][6:8]
        },
        "info_else" : {
            "name":f_split[0],
            "ext": f_split[-1]
        },
        "new_name": f_split[0]+"_"+f_split[1][6:8]+ "".join(["_" if len(f_split[2:-1])>0 else ""]+f_split[2:-1])
    }
    return info

def monthly_str(month_number):
    """
    It takes a month number as a string and returns the month name as a string
    
    :param month_number: The number of the month you want to convert to a string
    :return: The month number-name
    """
    translator = {
        "01":"01-January",
        "02":"02-February",
        "03":"03-March",
        "04":"04-April",
        "05":"05-May",
        "06":"06-June",
        "07":"07-July",
        "08":"08-August",
        "09":"09-September",
        "10":"10-October",
        "11":"11-November",
        "12":"12-December"
    }
    return translator[month_number]

def list_files(folder):
    """
    It returns a list of all files in a given folder
    
    :param folder: The folder to search for files in
    :return: A list of all files in the folder.
    """
    return list(folder.glob("**/*.*"))

def memories_sorter(src, dest, parser, keep_old=False):
    """
    It takes a source folder, a destination folder, a parser function and a boolean (keep_old) and sorts
    the files in the source folder into the destination folder by year and month
    
    :param src: The source folder where the memories are
    :param dest: The destination folder
    :param parser: a function that takes a file name and returns a dictionary with the following keys info_time, info_else and new_name
    :param keep_old: if True, the files will be copied to the new location, if False, they will be
    moved, defaults to False (optional)
    """
    file_list = list_files(src)
    print(len(file_list))
    loader = LoadingBar(len(file_list))
    for mem in file_list:
        name = mem.parts[-1]
        parsed_name = parser(name)
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
        new_name = parsed_name["new_name"] +"." + parsed_name["info_else"]["ext"]

        # Check if the file already exists in dest/year/month
        number = 1
        while Path(dest, year, month, new_name).exists():
                new_name = parsed_name["new_name"] + "_" + str(number) + "." + parsed_name["info_else"]["ext"]
                number += 1
        # Copy the file
        if keep_old :
            shutil.copy2(mem, Path(dest, year, month, new_name))
        else :
            mem.rename(Path(dest, year, month, new_name))
        loader.update()
    loader.finish()

current_repository = Path('./src')
aim_repository = Path('./dest')

memories_sorter(current_repository, aim_repository, format_wa_parser, keep_old=False)