#99乘法表
for i in range(10):
    for j in range(i):
        print('|',end=' ')
        print(i,'x',j,'=',i*j,end=' ')
    print()
