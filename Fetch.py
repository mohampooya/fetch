import os
import shutil
import easygui

path = easygui.diropenbox("enter your path to scan")
fileformat = easygui.choicebox('pick a format','format',['.pdf','.txt','.jpg','.png','.csv','.py','.dcm','none of the above'])
if fileformat == 'none of the above':
    fileformat = easygui.enterbox('enter the format you want like this : ".jpg"')
destpath = easygui.diropenbox('choose output path',)
for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        full_path = os.path.join(dirpath, filename)
        if filename.endswith(fileformat):
            shutil.copy(full_path, destpath)