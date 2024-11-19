# function for finding day
def findDay (num , name):
    born_day = num * 365
    greeting = f'Hello my name is {name} , and i have been born {born_day} days'
    return greeting
# ask user's name
inputName = input("enter your name \n:")
# calling fucntion and initailze the augument
print(findDay(20, inputName ))

    