# Machine Learning Support

from sklearn import svm
from sklearn.metrics import classification_report, confusion_matrix

# SVM LINEAR CLASSIFIER

def model(x_train,y_train):
    classifier = svm.SVC(kernel = 'linear')
    classifier.fir(x_train,y_train)
    return classifier

def test(classifier,x_test,y_test):
    prediction = classifier.predict(x_test)
    print("Confusion Matrix for given SVM Linear Model  : ")
    print(confusion_matrix(y_test,prediction))
    print("Classification Report for given SVM Linear Model : ")
    print(classification_report(y_test,prediction))
    return

def predict(classifier,features):
    prediction = classifier.predict(features)
    return prediction
