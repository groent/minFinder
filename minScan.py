import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import csv


#"GUI"
# print("--- minScan ---\n\nTo begin choose what file you would like to analyze.")
# file_name = input("Choose file name:\n> ")


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



