#Train-Valid Partitioning
from shutil import copy2
import random
from glob import glob
import os
random.seed(17)

# This is the path where our dataset is stored
path = 'Dataset/Skin_Diseases'
# These are the paths where we intend to store our train & valid sets
valid = 'Dataset/Valid'
train = 'Dataset/Train'

if not os.path.exists(valid):
	os.makedirs(valid)
if not os.path.exists(train):
	os.makedirs(train)
# glob module is used to retrieve files/pathnames matching a specified pattern 
for folder in glob(path+'/*'):
	print(folder)

	# find number of images in folder
	no_images_in_folder = len(os.listdir(folder))
	print("no of images in this folder: {}".format(no_images_in_folder))

	# make new folder inside test and train
	folder_valid = valid+'/'+folder.split('\\')[1]+'/'
	folder_train = train+'/'+folder.split('\\')[1]+'/'
	print(folder_valid)
	print(folder_train)

	if not os.path.exists(folder_valid):
		os.makedirs(folder_valid)
	if not os.path.exists(folder_train):
		os.makedirs(folder_train)

	print('---------------------------------------------\n')

	#Divide the images in Datase to Train set & valdi set by 0.8 : 0.2 ratio
	valid_num = int(no_images_in_folder*0.25)
		
	# Shuffle the data in the folder to divide evenly
	x = list(enumerate(glob(folder+'/*')))
	random.shuffle(x)

    # iterate from 0 to valid_num and copy to valid_folder
	# iterate valid_num to end and copy to train_folder
	count = 0
	for idx, im in x:
		if count <= valid_num:
		# copy to valid
			copy2(im, folder_valid)
			count += 1
		else:
		# copy to train
			copy2(im, folder_train)
			count += 1