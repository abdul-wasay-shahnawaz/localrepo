# Function - Scope of Variable
# LEGB Rule

### Global 
##def func():
##    print(x)
##
##x = 50   # Global variable
##
##func()

### Local 
##def func():
##    x = 50  # Local Variable
##    print(x)
##
##
##func()


### Enclosing
##def outer():
##    x = 30     # Enclosing Variable
##    #
##    #
##    #
##    
##    def inner():
##        print(x)
##
##    inner()
##
##outer()


# LEG Combination

def outer():
    x = 5   # Enclosing
    def inner():
        x = 10  # Local
        print("Inner x: ",x)  # 10  --> sECOND PRINT 

    print("Outer x: ", x)  # 5   --> fIRST PRINT
    inner()

x = 20  # Global 
outer()
print("Global x: ", x)   # 20  --> Third print
