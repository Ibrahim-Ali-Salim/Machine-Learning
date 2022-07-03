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




files=[]    
for i in range(len(file_list_Full_path)):
    if len(file_list_Full_path[i])>1:
        for k in range(len(file_list_Full_path[i])):
            file_list_Full_path[i][k]=path_list[i]+'\\'+file_list_Full_path[i][k]
            
file_list = [e for e in file_list if e]    
file_list=[x for x in file_list if len(x)>1]    

file_list_Full_path = [e for e in file_list_Full_path if e]    

file_list_Full_path=[x for x in file_list_Full_path if len(x)>1]    


###########################################################



from nilearn import datasets

dataset =  datasets.fetch_atlas_aal()
atlas_filename = dataset.maps
labels = dataset.labels

from nilearn import plotting
from matplotlib import pyplot as plt


from nilearn.input_data import NiftiLabelsMasker
from nilearn.connectome import ConnectivityMeasure
masker = NiftiLabelsMasker(labels_img=atlas_filename, standardize=True,
                           memory='nilearn_cache', verbose=5)


import numpy as np
from nilearn import plotting
import matplotlib.pyplot as plt
import scipy
import pandas as pd

df = pd.read_csv('csv file path')
Save_correlation_matrices_path ='Save path'
count=0
for i in range(0,len(file_list_Full_path)):
    try:
        time_series = masker.fit_transform(file_list_Full_path[i])
        print('i = ',i)
        valid_subjects.append(i)
        print('time_series shape = ',time_series.shape)
        correlation_measure = ConnectivityMeasure(kind='correlation')
        correlation_matrix = correlation_measure.fit_transform([time_series])[0]

        save_path =Save_correlation_matrices_path +'/'+file_list[0][i][:-7]+'.mat'
        scipy.io.savemat(save_path, {'correlation': correlation_matrix})
        count+=1
        
        
    except:
        pass
    else:
        continue

print('count=  ',count)

        

MAT_main_path ='Mat_files path'

MAT_file_list = []

for path, directories, files in os.walk(MAT_main_path):
    MAT_file_list.append(files)

print('Done file list')
MAT_file_list = [e for e in MAT_file_list if e]    



