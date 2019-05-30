for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            if(i!=j)and(j!=k)and(k!=i):
                a=str(i)+str(j)+str(k)
                print(a)