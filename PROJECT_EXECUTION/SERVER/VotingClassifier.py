# Machine Learning Support
# sklearn module imported for Machine Learning
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.metrics import classification_report, confusion_matrix

# VOTING CLASSIFIER

# Voting on KNN, Naive Bayes, Linear SVM, Poly SVM, Rvb SVM , Sigmoid SVM,

# Method to create a Classifier model 
def model(x_train,y_train):
    naivebayes = GaussianNB()
    # Naive Bayes model
    knearest = KNeighborsClassifier(n_neighbors = 7)
    #KNearest model
    linearsvm = svm.SVC(kernel = 'linear')
    #Linear SVM model
    polysvm = svm.SVC(kernel = 'poly')
    # PolySVM model
    rvbsvm = svm.SVC()
    # rvb SVM model
    sigmoidsvm = svm.SVC(kernel = 'sigmoid')
    # sigmoid SVM model
    decisiontree = DecisionTreeClassifier()
    # decision Tree Classifier model
     
    estimators=[ ('naive',naivebayes),('decisiontree',decisiontree)
                ,('knearest',knearest),('linearsvm',linearsvm)
                ,('polysvm',polysvm),('rvbsvm',rvbsvm)
                ,('sigmoidsvm',sigmoidsvm) ]    
    # Creating a estimators list for Voting Classifier
    voteClassifier = VotingClassifier(estimators,voting= 'hard')
    voteClassifier = voteClassifier.fit(x_train,y_train)
    return voteClassifier
    # Voting Classifier returned
    
# Method to Test the Model created    
def test(voteClassifier,x_test,y_test):
    prediction = voteClassifier.predict(x_test)
    print("Confusion Matrix for Vote Classifier Model given : ")
    print(confusion_matrix(y_test,prediction))
    print("Classification Report for given Vote Classisifer Model : ")
    print(classification_report(y_test,prediction))
    return
# Method to Predict the Testing
def predict(classifier,features):
    prediction = classifier.predict(features)
    return prediction
