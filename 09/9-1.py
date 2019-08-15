import numpy as np
from matplotlib import pyplot as plt

A = np.array([[5],[4]])
C = np.array([[4],[6]])
B = A.T.dot(C)
AA = np.linalg.inv(A.T.dot(A))
l = AA.dot(B)
P = A.dot(1)
x = np.linspace(-2,2,10)
x.shape = (1,10)
xx = A.dot(x)
fig = plt.figure()
a = fig.add_subplot(111)
a.plot(xx[0,:],xx[1,:])
a.plot(A[0],A[1],'ko')
a.plot([C[0],P[0]],[C[1],P[1]],'r-o')
a.plot([0,C[0]],[0,C[1]],'m-o')

a.axvline(x=0,color='black')
a.axhline(y = 0,color = 'black')

margin = 0.1
a.text(A[0]+margin,A[1]+margin,r"A",fontsize=20)
a.text(C[0]+margin,C[1]+margin,r"C",fontsize=20)
a.text(P[0]+margin,P[1]+margin,r"P",fontsize=20)
a.text(0+margin,0+margin,r"O",fontsize=20)
a.text(0+margin,4+margin,r"y",fontsize=20)
a.text(4+margin,0+margin,r"x",fontsize=20)
plt.xticks(np.arange(-2,3))
plt.yticks(np.arange(-2,3))

a.axis('equal')
plt.show()