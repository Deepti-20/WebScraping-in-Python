import json
with open("web_task5.json","r") as file1:
    data1=json.load(file1)
    # print(data1)
def analyse_movies_language(data):
    dict={}
    list1=[]
    for i in data:
        for j in i:
            if j =="langauge":
                list1.append(i[j])
            # print(li)
    count=0
    index=0
    for index in range(0,len(list1)):
        for i in range (0,len(list1)):
            if list1[index]==list1[i]:
                count+=1
        if list1[index] not in dict:
            dict[list1[index]]=count
    # print(dict)
    with open("web_task6.json","w") as file:
        json.dump(dict,file,indent=4)
analyse_movies_language(data1)