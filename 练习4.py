'''输入一个日期查询是该年的第几天'''
year=int(input("请输入年"))
month=int(input("请输入月"))
day=int(input("请输入日"))
Days=''
Days1=''
Days2=''
if 0<month<=12:
    days=[0,31,59,90,120,151,181,212,242,273,304,334]
    Days1=days[month-1]
normal=0
if (year%400==0)or( (year%4==0)and(year%400!=0)):
    normal=1
if (normal==1)and(month>2):
    Days2=Days1+1
    Days=Days2+day
else:
    Days=Days1+day
print("你输入的是"+str(year)+"年"+str(month)+"月"+str(day)+"日")
print('是你输入日期的第'+str(Days)+'天')