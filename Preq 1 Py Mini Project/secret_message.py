import os
import string
from string import digits


def rename_files():
    file_names = os.listdir(r"C:\Users\SARIM\Desktop\prank")

    # print(file_names)
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\SARIM\Desktop\prank")
    for old_name in file_names:
        temp = str.maketrans('', '', digits)
        new_name = old_name.translate(temp)
        os.rename(old_name, new_name)
    os.chdir(saved_path)


rename_files()
