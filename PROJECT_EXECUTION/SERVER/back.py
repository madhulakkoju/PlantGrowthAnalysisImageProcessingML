#import pandas as pd
from file1 import *
from xlsxwriter import *

rowcount = -1
ww = Workbook("featuredata.xlsx")
wsheet = ww.add_worksheet("train")

# fill_hist used to take a histogram array and add to rows in excel file
def fill_hist(hist,rec):
    for i in range(0,64):
        #print(i)
        wsheet.write(rowcount,rec,hist[i])
        rec = rec + 1
        #print(i)
    return
#fillin method is used to full the list into a row in excel file.
def fillin(vals):
    n = len(vals)
    for i in range(0,n):
        #print(vals[i],end = "  ")
        #print(features[i])
        wsheet.write(rowcount,i,vals[i])
    #print(vals[-1])
    #fill_hist(vals[-2],n-2)
    return

#  leafsnap-dataset-images
# Filling the data details into excel file.
with open('leafsnap-dataset-imageskart.txt') as readfile:
    for line in readfile:
        if rowcount == -1:
            rowcount = 0
            continue
        tabsplit = line.split("\t")
        if(len(tabsplit)<3):
            continue
        try:
            cv2.imread(tabsplit[1],0)
        except FileNotFoundError:
            print("Wrong file or file path")
            continue
        else:
            #Feature set is obtained by calling Feature extract method
            features = FeatureExtract(tabsplit[1])
            features.append((tabsplit[-3]+" "+tabsplit[-1]).lower())
            fillin(features)
            #Features are being filled into the file
            rowcount = rowcount + 1
ww.close()

            
