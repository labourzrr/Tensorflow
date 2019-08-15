import os
path = 'jpg'
filenames = os.listdir(path)
strText = ""

with open("train_list","w") as fid :
    for i in range(len(filenames)):
        strText = path + os.sep + filenames[i] + "," + filenames[i].split('_')[0] + "\n"
        fid.write(strText)
fid.close()