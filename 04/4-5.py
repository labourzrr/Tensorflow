import pandas as pd
import matplotlib.pyplot as plot

rockVMines = pd.DataFrame([[1,120,105,3,False],[2,165,80,2,False],[3,184.5,120,2,False],[4,116,70.8,1,False],[5,270,150,4,True]])

dataRow1 = rockVMines.iloc[1,0:3]
dataRow2 = rockVMines.iloc[2,0:3]
plot.scatter(dataRow1,dataRow2)
plot.xlabel("Attribute1")
plot.ylabel("Attribute2")
plot.show()

dataRow3 = rockVMines.iloc[3,0:3]
plot.scatter(dataRow2,dataRow3)
plot.xlabel("Attribute2")
plot.ylabel("Attribute3")
plot.show()