# Machine Learnig Support

from sklearn.tree import DecisionTreeClassifier
from metrics import accuracy_score,confusion_matrix,classification_report

# Decision Tree Classsiforer

def model(x_train,y_train):
    classifier = DecisionTreeClassifier()
    classifier = classifier.fit(x_train,y_train)
    return classifier

def test(classifier,x_test,y_test):
    prediction = classifier.predict(x_test)
    print("Confusion Matrix for Decision tree Classofier Model given : ")
    print(confusion_matrix(y_test,prediction))
    print("Classification Report for given Decision tree Classisifer : ")
    print(classification_report(y_test,prediction))
    print("Accuracy Score  : ",accuracy_score(y_test,prediction))
    return

def predict(classifier,features):
    prediction = classifier.predict(features)
    return prediction
