import os

main_path =  'Your path'

path_list =[[]]
file_list = [[]]
file_list_Full_path = [[]]

for path, directories, files in os.walk(main_path):
    path_list.append(path)

    file_list.append(files)

print('File list is done')

for path, directories, files in os.walk(main_path):
    file_list_Full_path.append(files)

print('File list Full path is done')
