import csv
import json
from datetime import datetime
import pandas as pd

df = pd.read_csv('Incision_Time\\data12-67.csv', delimiter=',')
df2 = pd.read_csv('Incision_Time\\dateCheck.csv', delimiter=',')

list_of_csv = [list(row) for row in df.values]
check = [list(row) for row in df2.values]

t = []
for i in range(len(check)):
  t.append(check[i][0])

max_day = list_of_csv[-1][1]
#max_day = 6

new_data = []
for i in list_of_csv:
  if i[10] < 0:
    tmp = i[7]
    i[7] = i[8]
    i[8] = tmp
    i[3] = 888
  elif i[10] == 0:
    i[3] = 999

  if i[1] <= max_day and i[3] != 999:
    check_emer = False
    for k in range(len(check)):
      if i[0] == check[k][0]:
        check_emer = True
        s_t = datetime.strptime(i[7], '%H:%M:%S')
        l_s = datetime.strptime(check[k][4], '%H:%M:%S')
        l_e = datetime.strptime(check[k][5], '%H:%M:%S')
        if s_t < l_s:
          # print(i[2]+ " " + i[0] + " before")
          tmp=0
        elif s_t >= l_s and s_t <= l_e:
          new_data.append([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], "in"])
          print(i[2]+ " " + i[0] + " in")
        elif s_t > l_e:
          new_data.append([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], "out"])
          print(i[2]+ " " + i[0] + " out")
    if check_emer == False:
      new_data.append([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], "emergency"])
      print(i[2]+ " " + i[0] + " emergency")


print("-------------------------------")

real = []

date = ' '
room = ' '
s_in = False
s_out = False
s_emer =  False
for dt in new_data:
  if date != dt[2]:
    date = dt[2]
    if room != dt[0]:
      room = dt[0]
      s_in = False
      s_out = False
      s_emer =  False
      if dt[11] == "in" :
        if s_in == False:
          print(dt[2]+ " " + dt[0] + " in")
          real.append([dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6], dt[7], dt[8], dt[9], dt[10], dt[11]])
          s_in = True
      elif dt[11] == "out":
        if s_in != True:
          print(dt[2]+ " " + dt[0] + " out")
          real.append([dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6], dt[7], dt[8], dt[9], dt[10], dt[11]])
          s_in = True
          s_out = True
        else:
          s_out = True
      else:
        if s_emer == False:
          print(dt[2]+ " " + dt[0] + " emer")
          real.append([dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6], dt[7], dt[8], dt[9], dt[10], dt[11]])
          s_emer = True
    else:
      if dt[11] == "in":
        if s_in == False:
          print(dt[2]+ " " + dt[0] + " in")
          real.append([dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6], dt[7], dt[8], dt[9], dt[10], dt[11]])
          s_in = True
      elif dt[11] == "out":
        if s_in != True:
          print(dt[2]+ " " + dt[0] + " out")
          real.append([dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6], dt[7], dt[8], dt[9], dt[10], dt[11]])
          s_in = True
          s_out = True
        else:
          s_out = True
      else:
        if s_emer == False:
          print(dt[2]+ " " + dt[0] + " emer")
          real.append([dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6], dt[7], dt[8], dt[9], dt[10], dt[11]])
          s_emer = True
  else:
    if room != dt[0]:
      room = dt[0]
      s_in = False
      s_out = False
      s_emer =  False
      if dt[11] == "in":
        if s_in == False:
          print(dt[2]+ " " + dt[0] + " in")
          real.append([dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6], dt[7], dt[8], dt[9], dt[10], dt[11]])
          s_in = True
      elif dt[11] == "out":
        if s_in != True:
          print(dt[2]+ " " + dt[0] + " out")
          real.append([dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6], dt[7], dt[8], dt[9], dt[10], dt[11]])
          s_in = True
          s_out = True
        else:
          s_out = True
      else:
        if s_emer == False:
          print(dt[2]+ " " + dt[0] + " emer")
          real.append([dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6], dt[7], dt[8], dt[9], dt[10], dt[11]])
          s_emer = True
    else:
      if dt[11] == "in":
        if s_in == False:
          print(dt[2]+ " " + dt[0] + " in")
          real.append([dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6], dt[7], dt[8], dt[9], dt[10], dt[11]])
          s_in = True
      elif dt[11] == "out":
        if s_in != True:
          print(dt[2]+ " " + dt[0] + " out")
          real.append([dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6], dt[7], dt[8], dt[9], dt[10], dt[11]])
          s_in = True
          s_out = True
        else:
          s_out = True
      else:
        if s_emer == False:
          print(dt[2]+ " " + dt[0] + " emer")
          real.append([dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6], dt[7], dt[8], dt[9], dt[10], dt[11]])
          s_emer = True

print(real)

fields =['mix_text','day','operdate','oper_location','oper_room','startdatetime','enddatetime','starttime','endtime','datenumber','cal', 'status']
# with open('Incision_Time\\GFG.csv', 'w') as f:
#
#   # using csv.writer method from CSV package
#   write = csv.writer(f)
#
#   write.writerow(fields)
#   write.writerows(real)

with open('Incision_Time\\GFG.csv', 'w', newline='') as f:
  write = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
  write.writerow(fields)
  write.writerows(real)

print("Done")