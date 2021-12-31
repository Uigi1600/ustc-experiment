#pre-proceed
import pandas as pd
import numpy as np
file = pd.read_excel("1.xls")
alpha = np.array(file["旋光"].tolist())
T = file["样品池温度"]
t = file["时间"].tolist()
t = [str(i) for i in t]
t = [str.split(i,sep=" ")[1] for i in t]
for i in range(len(t)):
    count = [float(j) for j in str.split(t[i],sep=":")]
    t.append(count[0]*3600+count[1]*60+count[2]) #Unit: s
t = t[75:]
t = np.array(t) - t[0]
record = []
for i in range(len(t)):
    if abs(T[i]-30) > 0.02:
        record.append(i)
t = np.delete(t,record)
alpha = np.delete(alpha,record)
t_ori = 2*60+14 #Unit: s (begin: 02:14:06)
t = t + t_ori
out = pd.DataFrame(data={"time":t,"alpha":alpha})
out.to_csv("1.csv",index=False)

#pre-proceed
import pandas as pd
import numpy as np
file = pd.read_excel("2.xls")
alpha = np.array(file["旋光"].tolist())
T = file["样品池温度"]
t = file["时间"].tolist()
t = [str(i) for i in t]
t = [str.split(i,sep=" ")[1] for i in t]
for i in range(len(t)):
    count = [float(j) for j in str.split(t[i],sep=":")]
    t.append(count[0]*3600+count[1]*60+count[2]) #Unit: s
t = t[int(len(t)/2):]
t = np.array(t) - t[0]
record = []
for i in range(len(t)):
    if abs(T[i]-35) > 0.04:
        record.append(i)
t = np.delete(t,record)
alpha = np.delete(alpha,record)
t_ori = 60+45 #Unit: s (begin: 01:45:24)
t = t + t_ori
time = []
for i in t:
    time.append(str(int(i/60))+":"+str(int(i%60))) #min:sec
out = pd.DataFrame(data={"time":t,"alpha":alpha})
out.to_csv("2.csv",index=False)
