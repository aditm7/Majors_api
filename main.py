import json
import pandas as pds
import math

data = pds.read_excel("Data.xlsx")
courses = {}
slots = ["8:15-10:15","11:15-13:15","14:15-16:15","17:15-19:15","20:15-22:15"]

for i in range (0,len(data),1):
  for s in slots:
    name = str(data[s].iloc[i])
    if len(name)!=3:
      name=name[:6]
      if name in courses:
        courses[name]["LHCs"].append(data["Venue"].iloc[i])
      else:
          courses[name]={"Day":int(data["Date"].iloc[i]),"LHCs":[],"Time":s}
          courses[name]["LHCs"].append(data["Venue"].iloc[i])

with open("majors.json","w") as f:
    json.dump(courses, f)