#NameError

#defination :
''' 
Handling NameError Exception in Python - Naukri Code 360
A NameError exception in Python occurs when the code attempts
to use a variable or function that has not been defined
or is not accessible in the current scope'''

try:
    print(x)
except NameError:
    print("Variable x is not defind")
except:
    print("Something else went wrong")