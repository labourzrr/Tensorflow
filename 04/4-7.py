import pandas as pd
import matplotlib.pyplot as plot

filePath = ("e://dataTest.csv")
dataFile = pd.read_csv(filePath,header = None,prefix = "V")

dataFile['V9'] = pd.to_numeric(dataFile['V9'],errors = 'coerce').fillna(0)

target = []
for i in range(100):
    if dataFile.iat[i,9] >= 7:
        target.append(1.0)
    else:
        target.append(0.0)

dataRow = dataFile.iloc[0:100,9]
plot.scatter(dataRow,target)
plot.xlabel("Attribute")
plot.ylabel("Target")
plot.show()