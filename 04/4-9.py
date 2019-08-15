from pylab import *
import pandas as pd
import matplotlib.pyplot as plot

filePath = ("e://dataTest.csv")
dataFile = pd.read_csv(filePath,header = None,prefix = "V")
dataFile['V1'] = pd.to_numeric(dataFile['V1'],errors = 'coerce').fillna(0)
dataFile['V2'] = pd.to_numeric(dataFile['V2'],errors = 'coerce').fillna(0)
dataFile['V3'] = pd.to_numeric(dataFile['V3'],errors = 'coerce').fillna(0)
dataFile['V4'] = pd.to_numeric(dataFile['V4'],errors = 'coerce').fillna(0)
dataFile['V5'] = pd.to_numeric(dataFile['V5'],errors = 'coerce').fillna(0)
dataFile['V6'] = pd.to_numeric(dataFile['V6'],errors = 'coerce').fillna(0)
dataFile['V7'] = pd.to_numeric(dataFile['V7'],errors = 'coerce').fillna(0)
dataFile['V8'] = pd.to_numeric(dataFile['V8'],errors = 'coerce').fillna(0)
dataFile['V9'] = pd.to_numeric(dataFile['V9'],errors = 'coerce').fillna(0)


dataFile.info()
print(dataFile.head())
print(dataFile.tail())

summary = dataFile.describe()
print(summary)

array = dataFile.iloc[:,3:9].values
boxplot(array)
plot.xlabel("Attribute")
plot.ylabel("Score")
plot.show()
