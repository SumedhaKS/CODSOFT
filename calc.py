# A Simple Calculator

#Functions
def add(a,b):
    return int(a)+ int (b)

def subtract(a,b):
    return int(a) - int(b)

def multiply(a,b):
    return int(a) * int(b)

def divide(a,b):
    if int(b)==0:
        print("Divisior cannot be Zero")
        return 'Undefined'
    else:
        return int(a) / int(b)


#Taking Inputs
a=input('Enter the first number:')
b=input('Enter the second number:')

#Selection of the operation
print("Select the operation to be performed\n")
operation=input('1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n \n')

#Displaying the Output
if operation=='1':
    print('\n', a,'+',b,'=', add(a,b))

elif operation=='2':
    print('\n', a,'-',b,'=', subtract(a,b))

elif operation=='3':
    print('\n', a,'*',b,'=', multiply(a,b))

elif operation=='4':
    print('\n', a,'/',b,'=', divide(a,b))

else:
    print("Invalid Option")
