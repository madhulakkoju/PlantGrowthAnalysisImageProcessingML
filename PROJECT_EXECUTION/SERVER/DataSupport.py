# Data Support for Machine Learning
#Importing required modules
import numpy as np
import pandas as pd
import xlrd
# xlrd for data storage and manipulations using excel
from sklearn.model_selection import train_test_split
#Using an Excel Sheet for Data Storage
location = str("featuredata.xlsx")
wb = xlrd.open_workbook(location)
# Opening the Excel sheet for Writing the data.
sheet  = wb.sheet_by_index(0)
# Setting the index to write at (0,0)
sheet.cell_value(0,0)
dataframe = pd.DataFrame([sheet.row_values(0)])
j = 0
while( j < sheet.nrows ):
    count = 50
    while(count > 0):
        dataframe.loc[len(dataframe)] = sheet.row_values(j)
        count = count - 1
        j = j + 1
        if(j>=sheet.nrows):
            break
print(dataframe)
# All the rows from the excel file are retrieved and a dataframe is created.
x = dataframe.iloc[:,:-1] 
print(x)
y = dataframe.iloc[:,-1]  #Considering Labels from Training dataset
print(y)

#   Data Set Splits 
x_train, x_test, y_train,y_test = train_test_split(x,y,test_size = 0.20)







