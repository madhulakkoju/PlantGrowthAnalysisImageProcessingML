# MachineLearning Model Application

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

# K Nearest Neigbors

# Creating a model for KNN

def model(x_train,y_train):
    classifier = KNeighborsClassifier(n_neighbors = 7) # for 7 nearest neighbors
    classifier.fit(x_train,y_train)
    return classifier

def test(classifier,x_test,y_test):
    prediction = classifier.predict(x_test)
    print("Confusion Matrix for KNN Model given : ")
    print(confusion_matrix(y_test,prediction))
    print("Classification Report for given KNN MOdel : ")
    print(classification_report(y_test,prediction))
    return

def predict(classifier, features):
    prediction = classifier.predict(features)
    return prediction



