# import time
# print(time.ctime())
import datetime
from datetime import datetime
from datetime import timedelta

current_time = datetime.now()
# print(current_time)
# print(type(current_time))

Modified_time = current_time.replace(microsecond=0)
# print(Modified_time)
# 2022-01-21 14:20:23
# %y-%m-%d %H:%M:%S

added_current_time = Modified_time + timedelta(minutes=330)
# print(added_current_time)
# print(type(added_current_time))

my_time_format = "%y_%m_%d_%H_%M_%S"

converted_format_time = datetime.strftime(Modified_time,my_time_format)
# print(converted_format_time)
# print(type(converted_format_time))


import tkinter
import os
from tkinter import filedialog
#pdf_in_file=open("simple.pdf",'rb')

root = tkinter.Tk()
root.withdraw()
file_name = filedialog.askopenfilename()
print(file_name)
base_file_name = os.path.basename(file_name)
print(base_file_name)

file_head,file_tail =os.path.split(file_name)
# print(file_head)
# print(file_tail)

base_file_alone = os.path.splitext(base_file_name)[0]
print(base_file_alone)
# pdf_in_file=open("file_name",'rb')
