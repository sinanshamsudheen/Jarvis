import pandas as pd

rf=pd.read_csv("D:\Time_Table.csv")

print(rf)
todays = rf[rf.Day=="Monday"]
print(todays)