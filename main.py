import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import csv

# Find Minima
#Get all the Lengths and Sort them from greatest to lowest
min_index = []
length_values = []
minima_values = []
min_time = []

df = pd.read_csv(f"Data/abi.csv")

#For each length find the minima
i = 0
size = len(df)
sliced_t = df.iloc[:, ::2]
sliced_P = df.iloc[:, 1::2]

for x in sliced_P:
   i = np.argmin(sliced_P[x])
   P = sliced_P[x]
   minima_values.append(P[i])
   min_index.append([i])
j = 0   
for x in sliced_t:
    s = sliced_t[x]
    min_time.append(s[min_index[j][0]])
    j+=1
    


#Extrapolate Length from Column Headers
for column_name in df.columns:
    #print(column_name)
    name = column_name.split()
    length = name[1][:-1]
    num = float(length)
    if num not in length_values:
        length_values.append(num)
    else:
        continue
    print(length)


#Sort Length values by their respective Minimum pressure

minima_per_length = []


for x in range(len(length_values)):
    arr = []
    arr.append(length_values[x])
    arr.append(min_time[x])
    arr.append(minima_values[x])
    minima_per_length.append(arr)


minima_per_length.sort(key=lambda x: x[0])
print(minima_per_length)

#plotting data
# fig, ax = plt.subplots(figsize=(10,7))

# ax.plot(minima_per_length[0],minima_per_length[1])
# ax.set_xlabel("Length (cm)", fontsize=14)
# ax.set_ylabel("Pressure (kPa)", fontsize=14)
# ax.set_title("Length vs Pressure Dip")

# plt.savefig("Length vs Min.png")



fields = ["Length (cm)", "Time (s)", "Pressure (kPa)"]
with open(f"Output/Length vs minPressure vs Time.csv", mode="a+", newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(fields)
    csvwriter.writerows(minima_per_length)
    file.close

#Find Maxima
#Get all the Lengths and Sort them from greatest to lowest
max_index = []
length_values = []
maxima_values = []
max_time = []


#For each length find the maxima
i = 0
size = len(df)
sliced_t = df.iloc[:, ::2]
sliced_P = df.iloc[:, 1::2]

for x in sliced_P:
   i = np.argmax(sliced_P[x])
   P = sliced_P[x]
   maxima_values.append(P[i])
   max_index.append([i])
j = 0   
for x in sliced_t:
    t = sliced_t[x]
    max_time.append(t[max_index[j][0]])
    j+=1

#Extrapolate Length from Column Headers
for column_name in df.columns:
    #print(column_name)
    name = column_name.split()
    length = name[1][:-1]
    num = float(length)
    if num not in length_values:
        length_values.append(num)
    else:
        continue
    print(length)

#Sort Length values by their respective Minimum pressure

maxima_per_length = []


for x in range(len(length_values)):
    arr = []
    arr.append(length_values[x])
    arr.append(max_time[x])
    arr.append(maxima_values[x])
    maxima_per_length.append(arr)


maxima_per_length.sort(key=lambda x: x[0])
print(maxima_per_length)


fields = ["Length (cm)", "Time (s)", "Pressure (kPa)"]
with open(f"Output/Length vs maxPressure vs Time.csv", mode="a+", newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(fields)
    csvwriter.writerows(maxima_per_length)
    file.close

#Find time from T_1 to T_2

difference = []
for x in range(len(length_values)):
    arr = []
    hitToRebound = max_time[x] - min_time[x]
    arr.append(length_values[x])
    arr.append(hitToRebound)
    difference.append(arr)
difference.sort(key=lambda x: x[0])

diffFields = ["Length (cm)", "Time (s)"]
with open(f"Output/Length vs Hit to Rebound (T1 to T2).csv", mode="a+", newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(diffFields)
    csvwriter.writerows(difference)
    file.close

# Find M1, M2 & M3

meanPerLength = []
k = 0
for x in sliced_P:
    i = np.mean(sliced_P[x])
    arr = []
    arr.append(length_values[k])
    arr.append(i)
    meanPerLength.append(arr)
    k+=1


pressure_differential = []
time_differential = []



print(pressure_differential)
print(time_differential)





#derivative = pressure_diff / time_diff


meanPerLength.sort(key=lambda x: x[0])
