import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
Sdata = pd.read_csv("C:/Users/MIR FAISAL/Downloads/Sonardata.csv",header = None)
print(Sdata.head())
print(Sdata.describe())
#print(Sdata[60].value_counts) #counts the number of rocks and mines in the 60th column
#separating data and labels
X = Sdata.drop(columns= 60, axis = 1) #data
Y = Sdata[60] #labels
#splitting the data
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.1,stratify=Y,random_state=1)
#print(X.shape,X_train.shape,X_test.shape)

model = LogisticRegression()
model.fit(X_train,Y_train)

#Accuravy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction,Y_train)
print("Accuracy on training Data: ", training_data_accuracy*100)
#accuracy on testing data
X_test_prediction = model.predict(X_test)
testing_data_accuracy = accuracy_score(X_test_prediction,Y_test)
print("Accuracy on testing data: ",testing_data_accuracy*100)

 #store the data here for rock or mine
input_data = (0.0200,0.0371,0.0428,0.0207,0.0954,0.0986,0.1539,0.1601,0.3109,0.2111,0.1609,0.1582,0.2238,0.0645,0.0660,0.2273,0.3100,0.2999,0.5078,0.4797,0.5783,0.5071,0.4328,0.5550,0.6711,0.6415,0.7104,0.8080,0.6791,0.3857,0.1307,0.2604,0.5121,0.7547,0.8537,0.8507,0.6692,0.6097,0.4943,0.2744,0.0510,0.2834,0.2825,0.4256,0.2641,0.1386,0.1051,0.1343,0.0383,0.0324,0.0232,0.0027,0.0065,0.0159,0.0072,0.0167,0.0180,0.0084,0.0090,0.0032)
input_data_as_numpy_array = np.asarray(input_data)
print(input_data_as_numpy_array)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
#print(input_data_reshaped) 
prediction = model.predict(input_data_reshaped)
print(prediction)
if(prediction[0] =='R' ):
    print("The object is a Rock")
else:
    print("The object is a mine")

 
