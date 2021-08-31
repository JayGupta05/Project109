import pandas as pd
import statistics
import csv

df = pd.read_csv("StudentsPerformance.csv")
performance = df["math score"].tolist()

mean = statistics.mean(performance)
mode = statistics.mode(performance)
median = statistics.median(performance)
sd = statistics.stdev(performance)

print(mean)
print(median)
print(mode)
print(sd)

sd1start,sd1end = mean-sd, mean+sd
sdresult = []

for score in performance:
    if(score>sd1start and score<sd1end):
        sdresult.append(score)

percent1 = len(sdresult)*100/len(performance)
print(percent1)

sd2start,sd2end = mean-2*sd, mean+2*sd
sdresult2 = []

for score in performance:
    if(score>sd2start and score<sd2end):
        sdresult2.append(score)

percent2 = len(sdresult2)*100/len(performance)
print(percent2)

sd3start,sd3end = mean-3*sd, mean+3*sd
sdresult3 = []

for score in performance:
    if(score>sd3start and score<sd3end):
        sdresult3.append(score)

percent3 = len(sdresult3)*100/len(performance)
print(percent3)