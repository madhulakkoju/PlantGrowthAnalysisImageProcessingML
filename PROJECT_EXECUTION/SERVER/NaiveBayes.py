# MachineLearning Model Application

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix

# Naive bayes Classifier model 

def model(x_train,y_train):
    model = GaussianNB()
    model.fit(x_train,y_train)
    return model

def test(model,x_test,y_test):
    prediction = model.predict(x_test)
    print("Confusion Matrix for given Naive Bayes Model  : ")
    print(confusion_matrix(y_test,prediction))
    print("Classification Report for given Naive Bayes Model : ")
    print(classification_report(y_test,prediction))
    return

def predict(model,features):
    prediction = model.predict(features)
    return prediction



























