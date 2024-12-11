#hi I've done that code about tic tac toe 
# I hope it is correct :)
from numpy import*
m = array([[str]*3]*3)
t = "X"

def remp(m):
    for i in range(3):
        for j in range(3):
            m[i,j] = "."
            
def aff(m):
    for i in range(3):
        if(i>=1):
            print("--------------------------")
        for j in range(3):
            print(m[i,j],end='   ')
def coc(m,t):
    n = int(input("input a number between 1-9 : "))
    i = loli(m,n)
    j = lolj(m,n)
    if(n>=1 and n<=9 and m[i,j]=="."):
        m[i,j] = t
        
        
        
        
        
def loli(m,n):
    c = 1
    for i in range(3):
        for j in range(3):
            if(c==n):
                return i
            else:
                c+=1
def lolj(m,n):
    c = 1
    for i in range(3):
        for j in range(3):
            if(c==n):
                return j
            else:
                c+=1
        
def switch(m,ok,t):
    if(t=="X"):
        return "O"
    else:
        return "X"
def end(m):
    if("." in m):
        return False
    else:
        return True

def sl(m,t):
    for i in range(3):
        if(ll(m,i,t)):
            return True
def ll(m,i,t):
    c = 0
    for j in range(3):
        if(m[i,j]==t):
            c+=1
    return c==3
def sc(m,t):
    for i in range(3):
        if(cc(m,i,t)):
            return True
def cc(m,i,t):
    c = 0
    for j in range(3):
        if(m[j,i]==t):
            c+=1
    return c==3
def sd(m,t):
    c = 0
    for i in range(3):
        if(m[i,i]==t):
            c+=1
    return c==3
def sdd(m,t):
    c = 0
    for i in range(3):
        if(m[i,3-i-1]==t):
            c+=1
    return c==3
        
        
    



t = "X"
remp(m)
aff(m)
ok = True
while(ok):
    coc(m,t)
    print("**************************************")
    aff(m)
    t =switch(m,ok,t)
    if(sl(m,"X") or sc(m,"X") or sd(m,"X") or sdd(m,"X")):
        print(f"the winner is X")
        break;
    elif(sl(m,"O") or sc(m,"O") or sd(m,"O") or sdd(m,"O")):
        print(f"the winner is O")
        break;
    elif(end(m)):
        print("No one has winned :(")
        ok = False

