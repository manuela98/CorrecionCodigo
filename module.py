import numpy

class Series(object):

    def __init__(self,N,a):
        self.N=N
        self.a=a
        n=len(a)
        
    def get_value(self,x):
        suma=0
        for n in range(self.N):
            suma+=self.a[n]*x**n
        return suma

    def get_derivative(self,x):
        deriv=0
        for n in range(1,self.N):
            deriv+=n*self.a[n]*x**(n-1)
        return deriv

    def getError(self,x,n):
        if n<0:
            raise ValueError(f"n should be larger than 0")
        elif n>self.N-1:
            raise ValueError(f"n should not be larger than {self.N}")
        else:
            error=x**(n+1)
            return error

    def Clean(self):
        #This funtion is only for seeing is system works
        from os import system
        system("ls 2> /dev/null")
        return 0
        
if __name__=="__main__":
    s=Series(3,[1,1/2,1/6])
    print(s.get_derivative(1))
