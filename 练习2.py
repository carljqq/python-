m=input("请输入你的利润：")
j=int(m)
'''将输入的数字转换成int型 '''
if (j<=10):
    n=j*0.1
elif(j>10)and(j<=20):
    n=(j-10)*0.075+1
elif(j>20)and(j<=40):
    n=1+10*0.075+(j-20)*0.005
elif(j>40)and(j<=60):
    n=1+10*0.075+20*0.05+(j-40)*0.03
elif(j>60)and(j<=100):
    n=1+10*0.075+20*(0.05+0.03)+(j-60)*0.015
elif j>100:
    n = 1 + 10 * 0.075 + 20 * (0.05 + 0.03) + 40 * 0.015+(j-100)*0.01
print(n)

