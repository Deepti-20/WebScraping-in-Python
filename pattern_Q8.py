# i=5
# while i>=1:
#     j=i 
#     while j>=1:
#         print(j,end=" ")
#         j=j-1
#     print()
#     i=i-1

# i=1
# while i<=5:
#     j=1 
#     while j<=i:
#         print(j,end=" ")
#         j=j+1
#     print()
#     i=i+1

# list1=[1,2,3,4,5,6,7,8]
# i=0
# length=len(list1)
# while i<length:
#     half=length//2
#     i=i+1
# print("lenght=",half)

# j=half
# lis=[]
# while j<len(list1):
#     lis.append(list1[j])
#     j=j+1
# print(lis)

# list1=[1,2,3,4,5,6,7]
# list2=[10, 20,30,40,50,60,70]
# list3=[100,200,300,400,500,600,700]
# i=0
# list4=[]
# while i< len(list1):
#     add=list1[i],list2[i],list3[i]
#     j=0
#     while j<len(add):
#         list4.append(add[j])
#         j=j+1
#     i=i+1
# print(list4)

# a=1
# b=2
# c= (str(a+b))
# # print("1 ""2")


# list1=['a','n','t','a','a','t','n','n','a','x','a','g','a','x','a']
# a=9
# b="deepti"
# print(a,b)

# list=[1,2,3,4,5,6,7,8,9,10]
# i=0
# while i<len(list):
#     j=0
#     while j<len(list):
#         j=j+1
#         i=i+1
# print()        


# lis=[0,5,7,0,1,0,8]
# count=0
# i=0
# while i<len(lis):
#     if lis[i]==0:
#         count=count+1
#     i=i+1
# print(count)


# i=0
# while True:
#     num=int(input("enter any num.."))
#     if num%2==0:
#         break
#     i=i+1

# dic1={"one":1,"two":2,"three":3,"four":4,"five":5}
# dic2={"name1":"deepu","age":20,"class":12,"id":"deepti@123"}
# dic3={"name1":"deepti","name2":"pooja","name3":"savita","name4":"amla"}
# i=0
# while i<len(dic1):




# list1=[1,['a',5,'5'],['ei',10,'true'],0]
# string=""
# i=0 
# while i<len(list1):
    
# list1=["neha","moni","sumit","doli"]
# i=-1
# length=len(list1)
# while i>=(-len(list1)):
#     print(list1[i])
#     i=i-1

# list=[[2,4,6],1,10]
# i=0
# sum=0
# while i<len(list):
#     # print(list[i])
#     j=0
#     while j<len(list[i]):
#         print(list[i][j])
#         # sum=sum+i
#         j=j+1
#     i=i+1
# print(sum)




# list1=[{"first":[2,4,6]},10,1]
# i=0
# lis1=[]
# while i<len(list1):
#     if type(list1[i])==int:
#         lis1.append(list1[i])
#     else:
#         for j in (list1[i]):
#             lis2=list1[i][j]
#     i=i+1
# lis1.extend(lis2)
# print(lis1)
# x=0
# sum=0
# while x<len(lis1):
#     sum=sum+lis1[x]
#     x=x+1
# print(sum)









# name={"num1":1,"num2":2,"num3":3}
# print(type(name))

# var='2.3'
# var1=23
# var2=float(var)
# print(var2+var1)

# a=5
# b=10
# c=a
# a=b
# b=c
# print(a,b)

# a=6
# b=1
# a=a+b
# b=a-b
# a=a-b
# print(a,b)

# p1=(1)
# p2=(3,4)
# p1+=1
# print(p1)

#compari
# x=5
# y=6
# z=x>y
# print(z)

#member
# name="deepti"
# print('y' in name)

#identity
# name1="deepti"
# name2="chhaya"
# print(name1 is name2)

#logical
# num1=int(input("enter any num.."))
# num2=int(input("enter any num.."))
# num3=int(input("enter any num.."))
# if num1>num2:
#     if num1>num3:
#         great=num1
#     else:
#         great=num3
        
# else: 
#     if num2>num1:
#         great=num2
#     else: 
#         great=num3
# print(great)
    

# A=[1,3,4,[5,7,[8,9],9,6],12,2]
# i=0
# sum=0
# while i<len(A):
#     if type(A[i])==int:
#         sum=sum+A[i]
#     else:
#         j=0
#         while j<len(A[i]):
#             if type(A[i][j])==int:
#                 sum=sum+A[i][j]
#             else:
#                 k=0
#                 while k<len(A[i][j]):
#                     sum=sum+A[i][j][k]
#                     k=k+1
#             j=j+1
#     i=i+1
# print(sum)

print("----------------------------------------")

# a=(3,4,53,4,7,55,8,22,14,37)
# i=0
# count=0
# count1=0
# while i<len(a):
#     if a[i]%2==0:
#         count=count+1
#     else:
#         count1=count1+1
#     i=i+1
# print(count,"even")
# print(count1,"odd")


# name=input("enter any name..")
# i=0
# while i<len(name):
#     print(name[i]*(i+1),end=" ")
#     i=i+1

# year=int(input("enter any year.."))
# month=int(input("enter any month.."))
# day=int(input("enter any date.."))
# if year>0:
#     if month>=1 and month<=12:
#         if day>=1 and day<=31:
#             print(year,month,day+1)
#         else:
#             print("There is no date greater than 31")
#     else:
#         print("there is no month greater than 12..")






# list1=[1,4,3,2,6,8,9,4,3,1,2,5,4,2,6]
# list2=[]
# count=0
# i=0
# while i<len(list1):
#     if list1[i] not in list2:
#         list2.append(list1[i])
#         # count=count+1
#         if len(count)>1 and len(count)<4: 
#     i=i+1
# print(list2)
# print(count)


# list1=[1,4,3,2,6,8,9,4,3,1,2,5,4,2,6]
# list2=[]
# i=0
# j=0
# count=0
# while i<len(list1):
#     if list1[i]==list1[j]:
#         count=count+1
#         # print(count)
#         j=j+1
#     i=i+1
# print(count)
    
      
# list1=[1,2,3,4,5]
# #O/P {1:{2:{3:{4:{5:{}}}}}}
# dic={}
# dic1={}
# dic2={}
# dic3={}
# dic4={}
# d={}
# # i=0
# # while i<len(list1):
# #     if [list1[i]]:
# dic[5]=d
# dic1[4]=dic
# dic2[3]=dic1
# dic3[2]=dic2
# dic4[1]=dic3

# print(dic4)
# # i=0
# # dic={}
# # while i<len(list1):
# #     list[i]=



# year=int(input("enter any year.."))
# month=int(input("enter any month.."))
# day=int(input("enter any date.."))
# if year>0:
#     if month>=1 and month<=12:
#         if day>=1 and day<=31:
#             print(year,month,day+1)
#         else:
#             print("There is no date greater than 31")
#     else:
#         print("there is no month greater than 12..")



# num=int(input("enter any number.."))
# num1=num
# reverse=0
# while num>0:
#     a=num%10
#     reverse=reverse*10+a
#     num=num//10
# if reverse==num1:
#     print(reverse,"palindrome")
# else:
    # print(reverse,"not palindrom


# big_list=[]
# i=1
# while i<=5:
#     dic={}
#     list1=[]
#     j=1
#     while j<=5:
#         multi=i*j
#         list1.append(multi)
#         j=j+1
#     dic[i]=list1
#     big_list.append(dic)
#     i=i+1
# print(big_list)

# def string_fun(string,end):
#     if string.endswith(end):
#         return "true"
#     else:
#         return "false"
# string=input("enter any word..")
# end=input("enter any letters..")
# print(string_fun(string,end))

# def string_fun(string,end):
#     a=len(end)
#     b=string[-a:]
#     print(a)
#     if b==end:
#         return "true"
#     else:
#         return "false"
# string=input("enter any word..")
# end=input("enter any letters..")
# print(string_fun(string,end))

# a='deepti "wonnao" '
# b=3
# print(a)

# x = 75
# def myfunc():
#     y = x + 1
#     print(x)

# myfunc()
# print(x)


# list1=[1,2,3,4,5,6]
# list2=[2,3,1,0,6,7]
# i=0
# while i<len(list1):
#     j=0
#     while j<len(list2):
#         if list1[i]  not in list2:
#             print(list1[i])
#         j=j+1
#         i=i+1

# list1=[1,2,3,4,5,6]
# list2=[2,3,1,0,6,7]
# i=0
# while i<len(list1):
#     if list1[i]  not in list2:
#         print(list1[i])
#     i=i+1

# number=[50,40,23,70,56,12,5,10,7]
# i=0
# while i<len(number):
#     i=i+1
# print(i)

# number=[50,40,23,70,56,12,5,10,7]
# count=0
# while number[count:]:
#     count=count+1
# print(count)


# list1=[[2,4,6,9],10,[3,8,12,19],57]
# l=[]
# sum1=0
# sum2=0
# i=0
# while i<len(list1):
#     if type(list1[i])==int:
#         if list1[i]%2==0:
#             sum1=sum1+list1[i]
#         else:
#             sum2=sum2+list1[i]
#         # l.append(list1[i])
#     else:
#         j=0
#         while j<len(list1[i]):
#             if list1[i][j]%2==0:
#                 sum1=sum1+list1[i][j]
#             else:
#                 sum2=sum2+list1[i][j]
#             # l.append(list1[i][j])
#             j=j+1
#     i=i+1
# # print(l)
# print(sum1)
# print(sum2)

# l=[1,2,3,4,5]
# # {1:{2:{3:{4:{5:{}}}}}}
# n = c = {}
# for i in l:
#     c[i] = {}
#     c = c[i]
# print(n)

# i=0
# while i<=5:
#     if i==3:
#         continue
#         print(i)
#     i=i+1

# i=0
# while i<=5:
#     i=i+1
#     if i==3:
#        continue
#     print(i)

# list1=[1,[1,2,3],2,[3,4,5],3,[6,7,8],4,[9,10,11]]
# i=0
# while i<len(list1):
#     if list1[i]==int:
#         print(list1[i])
#     # else:
#     #     j=0
#     #     while j<len(list1[i]):
#     #         multi=list1[i]*list1[j]
#     #         print(multi)
#     #         j=j+1    if num%2==0:
#         print("true")
#     else:
#         print("false")
# #     i=i+1


# num=int(input("enter any num.."))
# lis=[]
# i=0
# while num>i:
#     lis.append(num)
#     # if lis[i]%2==0:
#     #     print("true")
#     # else:
#     #     print("false")
#     print(lis)
#     i=i+1




# num=int(input("enter any number"))
# i=1
# while i<num:
#     j=0
#     while j<num:
#         print(j+1,end="")
#         j=j+1
#     print()
#     i=i+1


# i=1
# while i<=5:
#     j=1 
#     while j<=i:
#         print(i,end=" ")
#         j=j+1
#         print()
#         i=i+1


# list1=[[2,3,4],[2,4,5]]
# i=0
# while i<len(list1):
#     j=0
#     while j<len(list1[i]):
#         print(list1[i][j]+list1[i][j])
#         j=j+1
#         i=i+1

# n = int(input().strip())
# p = int(input().strip())
# def pageCount(n, p):
#     # n = int(input().strip())
#     # p = int(input().strip())
#     result = pageCount(n, p)
#     return result
# print(pageCount(n,p))


# txt = "     banana     "
# x = txt.strip()
# print("of all fruits", x, "is my favorite")

# n=int(input("enter any num.."))
# p=int(input("enter any number.."))
def pageCount(n, p):
    result=n-p-1
    return result
n=int(input("enter no. of page in book."))
p=int(input("enter on which page you want to go.."))
print(pageCount(n, p))
