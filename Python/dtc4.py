import numpy as np
import pandas as pd
from sklearn import *
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
df = pd.read_csv('data/schizoset.csv')
df["Obs_Sympt1"] = df["Obs_Sympt1"].map({'ImproperEyeContact':1 ,'ProperEyeContact':0})
df["Obs_Sympt2"] = df["Obs_Sympt2"].map({'NoIntimeResponse':1 ,'IntimeResponse':0})
df["Obs_Sympt3"] = df["Obs_Sympt3"].map({'ImaginativePlay':1 ,'NoImaginativePlay':0})
df["Obs_Sympt4"] = df["Obs_Sympt4"].map({'SpendsAlone':1 ,'SpendswithOthers':0})
df["Obs_Sympt5"] = df["Obs_Sympt5"].map({'Epilepsy':1 ,'NoEpilepsy':0})
df["Obs_Sympt6"] = df["Obs_Sympt6"].map({'Depression':1 ,'NoDepression':0})
df["Test_Sympt1"] = df["Test_Sympt1"].map({'PoorLogicalReasoning':1 ,'LogicalReasoningOK':0})
df["Test_Sympt2"] = df["Test_Sympt2"].map({'UnabletoSpeakSentns':1 ,'AbletoSpeakSentns':0})
df["Test_Sympt3"] = df["Test_Sympt3"].map({'UnabletoSpeakWords':1 ,'AbletoSpeakWords':0})
df["Test_Sympt4"] = df["Test_Sympt4"].map({'PoorinMaths':1 ,'NotpoorinMaths':0})
df["SchizoSeverity"] = df["SchizoSeverity"].map({'High':1 ,'Low':0})
data = df[["Obs_Sympt1","Obs_Sympt2","Obs_Sympt3","Obs_Sympt4","Obs_Sympt5","Obs_Sympt6","Test_Sympt1","Test_Sympt2","Test_Sympt3","Test_Sympt4","SchizoSeverity"]].to_numpy()
inputs = data[:,:-1]
outputs = data[:, -1]
training_inputs = inputs[:500]
training_outputs = outputs[:500]
testing_inputs = inputs[500:]
testing_outputs = outputs[500:]
classifier = DecisionTreeClassifier(max_depth=4)
classifier.fit(training_inputs, training_outputs)
predictions = classifier.predict(testing_inputs)
accuracy = 100.0 * accuracy_score(testing_outputs, predictions)
print ("The accuracy of DT Classifier with four levels on testing data is: " + str(accuracy))
testSet = [[0,0,1,1,0,0,1,0,0,1]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('DT prediction on the first test set is:',predictions)
testSet = [[0,0,1,0,1,1,1,0,0,1]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('DT prediction on the second test set is:',predictions)