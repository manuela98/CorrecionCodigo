import numpy

class Series(object):

    def __init__(self,nterms,a):
        self.nterms=nterms
        self.a=a

    def get_value(self,x):
        suma=0
        for n in range(self.nterms):
            suma+=self.a[n]*x**n
        return suma

    def get_derivative(self,x):
        deriv=0
        for n in range(1,self.nterms):
            deriv+=n*self.a[n]*x**(n-1)
        return deriv

    def get_error(self,x,n):
        if n<0:
            raise ValueError("n should be larger than 0")
        elif n>self.nterms-1:
            raise ValueError("n should not be larger than {self.nterms}")
        else:
            error=x**(n+1)
            return error

    def clean(self):
        #This funtion is only for seeing is system works
        from os import system
        system("ls 2> /dev/null")
        return 0
        
if __name__=="__main__":
    s=Series(3,[1,1/2,1/6])
    print(s.get_derivative(1))
