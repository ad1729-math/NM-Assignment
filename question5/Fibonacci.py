f0=1
f1=1


L=[f0]

def Fibo(n):
    A=f0
    B=f1
    for i in range(1,n):
       C=B
       B=B+A
       A=C
       L.append(C)
       
    return [B,L]



