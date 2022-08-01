import json,os

with open("web_task1.json","r") as file:
  task2=json.load(file)
  print(task2)  

def group_by_decade():
  list1=[]
  dic={}
  list2=[]
  for i in task2:
    # print(i)
    if (int(i['year'])) not in list1:
        list1.append(int(i['year']))
    list1.sort()
    # print(list1)

  for j in list1:
    if (j//10)*10 not in list2:
      list2.append((j//10)*10)
  # print(list2)
    
  for x in list2:
    list3=[]
    for y in task2:
      if x<=int(y['year'])<x+10:
        list3.append(y)
    dic[x]=list3
  return dic

decade= group_by_decade()


file=open("web_task3.json","w")
filedata=json.dump(decade,file,indent=4)













# def group_by_decade():
#   moviedic={}
#   list=[]
#   for i in task2:
#     print(i)
#     mod=i%10
#     dec=-i-mod
#     if dec not in list:
#       list.append(dec)
#   list.sort()
#   for i in list:
#     moviedic[i]=[]
#   for i in moviedic:
#     dec10=i+9
#     for x in task2:
#       if x<=dec10 and x>=i:
#         for v in task2[i]:
#           moviedic[i].append(v)
#   return moviedic
# group_by_decade()












