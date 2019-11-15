#!/usr/bin/env python 
# -*- coding:utf-8 -*-


import random

#模重复平方法+费马小定理实现素数检验

#模重复平方法
def fast_mod(b,n,m):
    two=bin(n)
    l=len(two)
    i=l-1
    a=1
    for j in range (1,l-1):
        if two[i]=='1':
            a=a*b % m

        b=(b**2)%m
        i=i-1
    return a



def prime_judge(n):
    for i in range (1,21):
        a=random.randint(2,n-1)
        flag=fast_mod(a,n-1,n)
        if flag!=1:
            return False
    return True



#随机生成大数+素数检验生成p,q
def get_prime():
    min=10**13
    max=10**14
    while(1):
        pri=random.randrange(min,max)
        if prime_judge(pri)==True:
            return pri


#求模反元素

#扩展欧几里得除法 ax+by=(a,b)
def ex_euclid(a,b):
    if b==0:
        return 1,0,a
    else:
        x,y,q=ex_euclid(b,a%b)
        x,y=y,(x-(a//b)*y)
    return x,y,q


def mod_inverse(e,n):
    temp=ex_euclid(e,n)
    d=temp[0]
    k=1
    if d<0:
        d=d+k*n

    return d

# def mod_inverse(e,n):           #求模反元素
#     if e==1 or n==1:
#         return 1
#     if e>n:
#         d=mod_inverse(e%n,n)
#         k=(e*d-1)//n
#         return k
#     else:
#         k=mod_inverse(e,n%e)
#         d=(1+n*k)//e
#         return d

#生成密钥

#最大公因式
def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)



def get_key():
    while(1):
        p=get_prime()
        q=get_prime()
        if p!=q:
            break

    n=p*q
    fai=(p-1)*(q-1)

    while(1):
        e=random.randrange(1,fai)
        if gcd(e,fai)==1:
            break



    d=mod_inverse(e,fai)

    return n , e , d  ,p,q

#加密
def encrypt(num,n,e):
    temp=fast_mod(num,e,n)
    return temp

#解密
def decode(num,n,d):
    temp=fast_mod(num,d,n)
    return temp

#密码系统
def RSA_pro(num):
    key=get_key()
    n=key[0]
    e=key[1]
    d=key[2]

    print("public key: n:",n ,"e:",e )
    print("private key: n:", n, "d:" ,d )


    pub_key=fast_mod(num,e,n )
    pri_key=fast_mod(pub_key,d,n )
    print("明文为：" ,pub_key)
    print("密文为：" ,pri_key)


if __name__=="__main__":
    m3=input()
    key=get_key()
    n=key[0]
    e=key[1]
    d=key[2]

    print("public key: n:",n ,"e:",e )
    print("private key: n:", n, "d:" ,d )


    #m3="Mathematical fundation of Information security+201904051+517021910722"
    #arr=m3.split(" ")

    arr=list(m3)
    #arr2="".join(arr)
    key=[]
    pub_key=[]
    pri_key=[]
    dec=[]

    l=len(arr)

    for i in range (0,l):
        key.append(ord(arr[i]))
        pub_key.append(fast_mod(key[i],e,n ))
        pri_key.append(fast_mod(pub_key[i],d,n ))
        dec.append(chr(pri_key[i]))

    arr2="".join(dec)
    print("密文为：" ,pub_key)
    print("明文为：" ,arr2)






