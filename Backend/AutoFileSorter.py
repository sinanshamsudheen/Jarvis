
import os
import shutil
# import tkinter as tk
from tkinter import messagebox
import sys
import time

path = r"C:/Users/zero/Downloads"
path2 = r"D:\IDM"

file_names = os.listdir(path)

folder_names = ['Video', 'Music', 'Documents', 'Compressed', 'Images','Programs','Books','Office','Subs','Others']

# Create folders if they don't exist
for folder in folder_names:
    folder_path = os.path.join(path2, folder)
    if not os.path.exists(folder_path):
        print(f"Creating folder: {folder_path}")
        os.makedirs(folder_path)

# Move files to respective folders
for file in file_names:
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):
        if file.endswith('.pdf') and not os.path.exists(os.path.join(path2, "Documents", file)):
            shutil.move(file_path, os.path.join(path2, "Documents", file))
        elif file.endswith('.docx') and not os.path.exists(os.path.join(path2, "Documents", file)):
            shutil.move(file_path, os.path.join(path2, "Documents", file))
        elif file.endswith('.txt') and not os.path.exists(os.path.join(path2, "Documents", file)):
            shutil.move(file_path, os.path.join(path2, "Documents", file))
        elif file.endswith('.mp3') and not os.path.exists(os.path.join(path2, "Music", file)):
            shutil.move(file_path, os.path.join(path2, "Music", file))
        elif file.endswith('.wav') and not os.path.exists(os.path.join(path2, "Music", file)):
            shutil.move(file_path, os.path.join(path2, "Music", file))
        elif file.endswith('.flac') and not os.path.exists(os.path.join(path2, "Music", file)):
            shutil.move(file_path, os.path.join(path2, "Music", file))
        elif file.endswith('.ogg') and not os.path.exists(os.path.join(path2, "Music", file)):
            shutil.move(file_path, os.path.join(path2, "Music", file))
        elif file.endswith('.mp4') and not os.path.exists(os.path.join(path2, "Video", file)):
            shutil.move(file_path, os.path.join(path2, "Video", file))
        elif file.endswith('.mkv') and not os.path.exists(os.path.join(path2, "Video", file)):
            shutil.move(file_path, os.path.join(path2, "Video", file))
        elif file.endswith('.avi') and not os.path.exists(os.path.join(path2, "Video", file)):
            shutil.move(file_path, os.path.join(path2, "Video", file))
        elif file.endswith('.zip') and not os.path.exists(os.path.join(path2, "Compressed", file)):
            shutil.move(file_path, os.path.join(path2, "Compressed", file))
        elif file.endswith('.rar') and not os.path.exists(os.path.join(path2, "Compressed", file)):
            shutil.move(file_path, os.path.join(path2, "Compressed", file))
        elif file.endswith('.png') and not os.path.exists(os.path.join(path2, "Images", file)):
            shutil.move(file_path, os.path.join(path2, "Images", file))
        elif file.endswith('.jpg') and not os.path.exists(os.path.join(path2, "Images", file)):
            shutil.move(file_path, os.path.join(path2, "Images", file))
        elif file.endswith('.jpeg') and not os.path.exists(os.path.join(path2, "Images", file)):
            shutil.move(file_path, os.path.join(path2, "Images", file))
        elif file.endswith('.exe') and not os.path.exists(os.path.join(path2, "Programs", file)):
            shutil.move(file_path, os.path.join(path2, "Programs", file))
        elif file.endswith('.epub') and not os.path.exists(os.path.join(path2, "Books", file)):
            shutil.move(file_path, os.path.join(path2, "Books", file))
        elif file.endswith('.pptx') and not os.path.exists(os.path.join(path2, "Office", file)):
            shutil.move(file_path, os.path.join(path2, "Office", file))
        elif file.endswith('.srt') and not os.path.exists(os.path.join(path2,"Subs",file)):
            shutil.move(file_path,os.path.join(path2,"Subs",file))
        elif file.endswith('.xlsm') and not os.path.exists(os.path.join(path2,"Office",file)):
            shutil.move(file_path,os.path.join(path2,"Office" , file))
        elif file.endswith('.xlam') and not os.path.exists(os.path.join(path2,"Office",file)):
            shutil.move(file_path,os.path.join(path2,"Office" ,file))
        elif file.endswith('.csv') and not os.path.exists(os.path.join(path2,"Office",file)):
            shutil.move(file_path,os.path.join(path2,"Office",file))
        elif file.endswith('.xlsx') and not os.path.exists(os.path.join(path2,"Office",file)):
            shutil.move(file_path,os.path.join(path2,"Office",file))
        else:
            shutil.move(file_path,os.path.join(path2,"Others",file))

print("Files have been organized.")
# tk.Tk().withdraw()
# messagebox.showinfo(title="Alert",message="Files were moved!")
# time.sleep(20)
sys.exit()
