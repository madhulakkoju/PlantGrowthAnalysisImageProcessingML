# K Nearest Neighbors implementation

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xlrd

loc = str("C:\\Users\\ADMIN\\Documents\\Python Scripts\\featuredata.xlsx")
wb = xlrd.open_workbook(loc)
sheet  = wb.sheet_by_index(0)
sheet.cell_value(0,0)
df = pd.DataFrame([sheet.row_values(0)])
buf=[]
j = 0

while(j < sheet.nrows):
    count = 50
    while(count > 0):
        #print(count,end ="-\n")
        df.loc[len(df)] = sheet.row_values(j)
        count = count - 1
        j = j + 1
        if(j>=sheet.nrows):
            break

print(df)
    
x = df.iloc[:,:-1].values
print(x)
y = df.iloc[:,-1]
print(y)
#=============================================================
#   Data Set Splits 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train,y_test = train_test_split(x,y,test_size = 0.50)
'''
print(x_train)
print(y_train)

print(x_test)
print(y_test)


#========================================================================

# K Nearest Neighbors

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5)
classifier.fit(x_train,y_train)
y_pred = classifier.predict(x_test)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print("\n\n====================  K Nearest neighbors  ======================\n\n")
#================================ DONE   ===================================

#   Decision Tree Classifier

from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier(min_samples_split = 28)
tree.fit(x,y)

print(f'Model Accuracy: {tree.score(x,y)}')

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

print("\n\n===============  Decision tree Classifier ===========\n\n")

#\==============================================================================
'
# Random Forest 

from sklearn.ensemble import RandomForestRegressor
randomForest = RandomForestRegressor(n_estimators = 1000,random_state = 42)
randomForest.fit(x_train,y_train)

pred = randomForest.predict(x_test)
correct = 0
wrong = 0
for i in rang(0,len(pred)) :
    if(pred[i]==
    

error = abs(pred - y_test)

print("Mean absolute error :",round(np.mean(error),2),'degrees')

print("\n\n===============  Random Forest   +==========\n\n")
'
#================================================================================


from sklearn import preprocessing

le = preprocessing.LabelEncoder()

#train_labels_encoded=le.fit_transform(y_train)
#test_labels_encoded = le.fit_transform(y_test)

#print(train_labels_encoded)

from sklearn.naive_bayes import GaussianNB

nbModel = GaussianNB()
#nbModel.fit(x_train,train_labels_encoded)
nbModel.fit(x_train,y_train)

preds = nbModel.predict(x_test)

print(preds)

from sklearn import metrics
print("Accuracy : ",metrics.accuracy_score( y_test,preds))
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print("\n\n================= Naive Bayes ==============\n\n")


#==============================================================================


# SVM Classifier linear

from sklearn import svm
clf = svm.SVC(kernel = 'linear')
clf.fit(x_train,y_train)
predic = clf.predict(x_test)

from sklearn import metrics

print("Accuracy : ",metrics.accuracy_score( y_test,predic))
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print("============= Linear SVC  SVM ===============")

#===============================================================================


# SVM Classifier poly

from sklearn import svm
clf = svm.SVC(kernel = 'poly')
clf.fit(x_train,y_train)
predic = clf.predict(x_test)

from sklearn import metrics

print("Accuracy : ",metrics.accuracy_score( y_test,predic))
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print("============= Poly SVC  SVM ===============")


#==========================================================================

# SVM Classifier rbf

from sklearn import svm
clf = svm.SVC(kernel = 'rbf')
clf.fit(x_train,y_train)
predic = clf.predict(x_test)

from sklearn import metrics

print("Accuracy : ",metrics.accuracy_score( y_test,predic))
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print("\n============= rbf SVC  SVM ===============\n\n")

#============================================================================
# SVM Classifier sigmoid

from sklearn import svm
clf = svm.SVC(kernel = 'sigmoid')
clf.fit(x_train,y_train)
predic = clf.predict(x_test)

from sklearn import metrics

print("Accuracy : ",metrics.accuracy_score( y_test,predic))
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print("============= sigmoid SVC  SVM ===============")
#============================================================================


#Voting Classifier
#uses the pre predicted data fromthe different clasifiers and votes among them to generate a value


from sklearn import metrics

from sklearn.naive_bayes import GaussianNB
clf1=GaussianNB()
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
clf2 = RandomForestClassifier(n_estimators=50, random_state=1)
from sklearn import svm
clf = svm.SVC(kernel = 'linear')


voting = VotingClassifier(estimators=[('gnb', clf1), ('rf', clf2), ('lsvm', clf)], voting='hard')
voting  = voting.fit(x_train,y_train)
votes = voting.predict(x_test)
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print("Accuracy : ",metrics.accuracy_score( y_test,votes))

print("======================== Voting Classifier  ==============================\n\n")
'''


import knn_ml_module as ml

classifier = ml.modelKNN(x_train,y_train)

ml.testKNN(classifier,x_test,y_test)
print(y_test)
print("===")
print(ml.predictKNN(classifier,x_test[0]))




















