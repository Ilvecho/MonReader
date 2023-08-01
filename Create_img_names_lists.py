import os 
import pickle

LOCALDIR = "C:\\Users\\massi\\source\\repos\\Project_4\\images"
CATEGORIES = ["\\flip", "\\notflip"]
print(os.listdir(LOCALDIR))

img_names = {}
for use in ["\\training", "\\testing"]:

  print(use.split('\\')[-1])
  for category in CATEGORIES: 
    path = ''.join([LOCALDIR,use,category])  # create path to the data
    tmp_list = []
    for img in os.listdir(path):  # iterate over each image
      tmp_list.append(img)

    split_name = use.split('\\')[-1] + '_' + category.split('\\')[-1]
    print(split_name)
    img_names[split_name] = tmp_list

handle = open(LOCALDIR + "img_names.pkl", "wb")
pickle.dump(img_names, handle)
