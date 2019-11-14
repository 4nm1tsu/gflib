#!/usr/bin/env python3
"""
File Name       : gflib3.py
Encoding        : utf-8
Creation Date   : 2019/10/21

Copyright © 2019 Hibiki Okada All rights reserved.

This source code or any portion thereof must not be
reproduced or used in any manner whatsoever.
"""
def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

def table(p,m,ply):
    tmp=p**m
    a=[1]#演算用
    ans=[]
    for i in range(m):
        a.append(0)
    for i in range(tmp-1):
        if a[-1]>=1:
            for j in range(a[-1]):
                for k in range(m):
                    a[k]=gf.gf_add(p,ply[k],a[k])
            ans.append(calc(a,p,m))
        else:
            ans.append(calc(a,p,m))
        a.pop()
        a.insert(0,0)
    ans.append(1)
    return ans

def calc(a,p,m):
    ans=0
    for i in range(m):
        ans+=(p**i)*a[i]
    return ans

class gf():
    #constant
    space=3
    def gf_add(p,a,b):
        return (a+b)%p
    def gf_sub(p,a,b):
        if (a-b)<0:
            return (a-b+p)%p
        else:
            return (a-b)%p
    def gf_mul(p,a,b):
        return (a*b)%p
    def ex_euclid(x, y):
        c0, c1 = x, y
        a0, a1 = 1, 0
        b0, b1 = 0, 1

        while c1 != 0:
            m = c0 % c1
            q = c0 // c1

            c0, c1 = c1, m
            a0, a1 = a1, (a0 - q * a1)
            b0, b1 = b1, (b0 - q * b1)

        return b0

    def gf_div(p,a,b):
        t=gf.ex_euclid(p,b)
        if t<0:
            i=1
            while (t+i*p)%p<0:
                i+=1
            t=(t+i*p)%p
        return (a*t)%p


    def set_space(a):
        gf.space=a
    def __init__(self,x):
        self.value=x
    def __repr__(self):
        return str(self.value)
    def __str__(self):
        return str(self.value)
    def __add__(self,y):
        if type(y) is int:
            y=gf(y)
        return gf(gf.gf_add(gf.space,self.value,y.value))
    def __sub__(self,y):
        if type(y) is int:
            y=gf(y)
        return gf(gf.gf_sub(gf.space,self.value,y.value))
    def __mul__(self,y):
        if type(y) is int:
            y=gf(y)
        return gf(gf.gf_mul(gf.space,self.value,y.value))
    def __truediv__(self,y):
        if type(y) is int:
            y=gf(y)
        return gf(gf.gf_div(gf.space,self.value,y.value))
    def __radd__(self,y):
        if type(y) is int:
            y=gf(y)
        return gf(gf.gf_add(gf.space,self.value,y.value))
    def __rsub__(self,y):
        if type(y) is int:
            y=gf(y)
        return gf(gf.gf_sub(gf.space,self.value,y.value))
    def __rmul__(self,y):
        if type(y) is int:
            y=gf(y)
        return gf(gf.gf_mul(gf.space,self.value,y.value))
    def __rtruediv__(self,y):
        if type(y) is int:
            y=gf(y)
        return gf(gf.gf_div(gf.space,self.value,y.value))

class gfex(gf):
    #constant
    P=3#係数
    M=2#mbit
    PLY=[1,2]#長さM
    TABLE=table(P,M,PLY)
    def set_const(p,m,ply):
        gf.space=p
        gfex.P=p
        gfex.M=m
        gfex.PLY=ply
        gfex.TABLE=table(gfex.P,gfex.M,gfex.PLY)
    def get_const():
        print('P=',gfex.P,'M=',gfex.M,'PLY=',gfex.PLY)
    def info():
        for i in range(gfex.P**gfex.M):
            print(gfex(i))
    def bin2dec(a):#引数はgfex.gfval
        #tmp1=copy.copy(list(a))
        tmp1=list(a)
        tmp2=[]
        for i in tmp1:
            tmp2.append(i.value)
        ans=0
        digit=0
        for i in tmp2:
            ans+=(gfex.P**digit)*(i)
            digit+=1
        return ans
    def dec2bin(a):#引数はint
        tmp=list(map(int,list(Base_10_to_n(a,gfex.P))))
        while len(tmp)<gfex.M:
            tmp.insert(0,0)
        tmp=tmp[::-1]
        ans=[]
        for i in range(gfex.M):
            ans.append(gf(tmp[i]))
        return ans

    def __init__(self,array):
        self.gfval=[]
        if type(array) is int:#int
            if array == -1:
                for i in range(gfex.M):
                    self.gfval.append(gf(0))
            else:
                tmp=gfex.dec2bin(gfex.TABLE[array])
                for i in tmp:
                    self.gfval.append(i)
        elif type(array[0]) is gf:#gf配列
            tmp=[]
            for i in array:
                tmp.append(i.value)
            if not any(tmp):#すべて0
                for i in range(gfex.M):
                    self.gfval.append(gf(0))
            else:
                for i in array:
                    self.gfval.append(i)
        else:#ただの配列
            if not any(array):
                for i in range(gfex.M):
                    self.gfval.append(gf(0))
            else:
                for i in array:
                    self.gfval.append(gf(i))
    def __repr__(self):
        tmp=[]
        for i in range(gfex.M):
            tmp.append(self.gfval[i].value)
        if not any(tmp):
            return str(self.gfval)+' '+'-1'
        else:
            return str(self.gfval)+' '+str(gfex.TABLE.index(gfex.bin2dec(self.gfval)))
    def __str__(self):
        tmp=[]
        for i in range(gfex.M):
            tmp.append(self.gfval[i].value)
        if not any(tmp):
            return str(self.gfval)+' '+'-1'
        else:
            return str(self.gfval)+' '+str(gfex.TABLE.index(gfex.bin2dec(self.gfval)))
        #return str(self.gfval)
    def __getitem__(self,key):
        return self.gfval[key]
    def __setitem__(self,key,value):
        self.gfval[key]=value
    def __add__(self,y):
        __tmp=[]
        for i in range(len(self.gfval)):
            __tmp.append((self.gfval[i]+y.gfval[i]).value)
        return gfex(__tmp)
    def __sub__(self,y):
        __tmp=[]
        for i in range(len(self.gfval)):
            __tmp.append((self.gfval[i]-y.gfval[i]).value)
        return gfex(__tmp)
    def __mul__(self,y):
        tmps=[]
        tmpy=[]
        for i in range(gfex.M):
            tmps.append(self.gfval[i].value)
        for i in range(gfex.M):
            tmpy.append(y.gfval[i].value)
        if not any(tmps):
            return gfex(-1)
        else:
            a=gfex.TABLE.index(gfex.bin2dec(self.gfval))
        if not any(tmps):
            return gfex(-1)
        else:
            b=gfex.TABLE.index(gfex.bin2dec(y.gfval))
        c=(a+b)%((gfex.P**gfex.M)-1)
        c=gfex.TABLE[c]
        ans=gfex.dec2bin(c)
        return gfex(ans)
    def __truediv__(self,y):
        tmps=[]
        tmpy=[]
        for i in range(gfex.M):
            tmps.append(self.gfval[i].value)
        for i in range(gfex.M):
            tmpy.append(y.gfval[i].value)
        if not any(tmpy):
            print('error')
            return -1
        else:
            b=gfex.TABLE.index(gfex.bin2dec(y.gfval))
        if not any(tmps):
            return gfex(-1)
        else:
            a=gfex.TABLE.index(gfex.bin2dec(self.gfval))
        if a<b:
            i=1
            while (a-b)+i*((gfex.P**gfex.M)-1)<0:
                i+=1
            c=(a-b)+i*((gfex.P**gfex.M-1))%((gfex.P**gfex.M))
        else:
            c=(a-b)%((gfex.P**gfex.M)-1)
        c=gfex.TABLE[c]
        ans=gfex.dec2bin(c)
        return gfex(ans)
