# main Function

def main():
    print("Hello")
    myFun(3020,18)
    yourFunc(1,2,3,4,5,6,7)

# Making Function 

def myFun(pin,age):
    print('My pin is {} and my age is {} '.format(pin,age))

# Multiple arguments

def yourFunc(one,two,*args):
    print("The values are {}, {}, {} ".format(one,two,args))

    # for i in args: print(args)

    # for j in args: print(j)

    ourFunc(1,2,3,4,5,onee = 'Monday' , twoo = 'Tuesday' , threee = 'Wednesday')

    #KWargs or known as Key Word Arguments

def ourFunc(a,b,c,*args,**kwargs):
    print("The value is {}, {}, {}, {}, {}".format(a,b,c,args,kwargs))
    print("Hello ",kwargs['onee'],kwargs['twoo'],kwargs['threee'])

    print(returnFunc())
    for i in returnFunc() : print(i, end=' ')

# Return of Function

def returnFunc():
    return range(10)

# Call Main Function 

if __name__ == "__main__" : main()