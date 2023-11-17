import numpy as np
import time
X = []
Y = []
cnt=1000
for i in range(1,cnt+1):
    X.append(i)

for i in range(1,cnt+1):
    Y.append(i)

X_array = np.array(X)
Y_array = np.array(Y)           #转变为列向量

print(X_array)
print(Y_array.reshape(cnt,1))     #给它转换为5*1矩阵
#下面是X_array是一个1*5的矩阵，而Y_array是一个5*1的矩阵了
t1 = time.time_ns()
#res_temp = np.dot(X_array,Y_array)
res_temp = np.sum(X_array*Y_array)
t2 = time.time_ns()
print("time: "+str(t2-t1)+"ns.")
print(res_temp)