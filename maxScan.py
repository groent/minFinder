import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import csv

#Get all the Lengths and Sort them from greatest to lowest
max_index = []
length_values = []
maxima_values = []
max_time = []

df = pd.read_csv(f"Data/abi.csv")

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
