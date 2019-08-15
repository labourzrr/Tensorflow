import pandas as pd
import random
import matplotlib.pyplot as plot

filePath = ("e://dataTest.csv")
dataFile = pd.read_csv(filePath,header = None,prefix = "V")

dataFile['V9'] = pd.to_numeric(dataFile['V9'],errors = 'coerce').fillna(0)

target = []
for i in range(100):
    if  dataFile.iat[i,9] >= 7:
        target.append(1.0 + random.uniform(-0.3,0.3))
    else:
        target.append(0.0 + random.uniform(-0.3,0.3))

dataRow = dataFile.iloc[0:100,9]
plot.scatter(dataRow,target)
plot.xlabel("Attribute")
plot.ylabel("Target")
plot.show()

dataFile['V1'] = pd.to_numeric(dataFile['V1'],errors = 'coerce').fillna(0)
dataFile['V2'] = pd.to_numeric(dataFile['V2'],errors = 'coerce').fillna(0)
dataFile['V3'] = pd.to_numeric(dataFile['V3'],errors = 'coerce').fillna(0)
dataFile['V4'] = pd.to_numeric(dataFile['V4'],errors = 'coerce').fillna(0)
dataFile['V5'] = pd.to_numeric(dataFile['V5'],errors = 'coerce').fillna(0)
dataFile['V6'] = pd.to_numeric(dataFile['V6'],errors = 'coerce').fillna(0)
dataFile['V7'] = pd.to_numeric(dataFile['V7'],errors = 'coerce').fillna(0)
dataFile['V8'] = pd.to_numeric(dataFile['V8'],errors = 'coerce').fillna(0)
dataFile['V9'] = pd.to_numeric(dataFile['V9'],errors = 'coerce').fillna(0)