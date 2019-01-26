''''
Lab 1:
 Iris dataset
'''

import pandas as pd
from matplotlib import pyplot as plt

file_name = "iris.csv"
data = pd.read_csv(file_name)
print(data.columns)

print(data.head())
#plt.plot(data['PetalWidthCm'],data['SepalWidthCm'])

species = set(data['Species'])
mean_values = pd.DataFrame()
var_values = pd.DataFrame()

for plant in species:
     mean_values[plant] = data[data['Species']== plant].mean()
     var_values[plant] = data[data['Species']== plant].var()

diff_virgin = data[data["Species"] == "Iris-virginica"].sub(mean_values["Iris-virginica"])
diff_versi = data[data["Species"] == "Iris-versicolor"].sub(mean_values["Iris-versicolor"])
diff_setosa = data[data["Species"] == "Iris-setosa"].sub(mean_values["Iris-setosa"])

plt.figure()
fig,ax=plt.subplots(2,2,figsize=(17, 8))
diff_virgin.plot(kind="hist", ax=ax[0][0],label="virgin",color
='r',fontsize=10)
diff_versi.plot(kind="hist", ax=ax[0][1],label="versi",color='b',fontsize=10)
diff_setosa.plot(
kind="hist",ax=ax[0][2],label="setosa",color='g',fontsize=10)
plt.show()
