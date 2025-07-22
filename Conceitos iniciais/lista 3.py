#ex 1
"""""
def inicio():
    num1 = float(input('choice one number: '))
    num2 = float(input('choice one number: '))
    div(num1, num2)

def div(n1,n2):
    if n2 !=0:
        print(n1 / n2)
    else:
        print('The second number cannot be zero...')

inicio()
"""""

#ex 2
"""""
const = 16
num_Usuario = float(input('enter your number: '))
verify = True

while verify:
    if num_Usuario != const:
        print('Try again...')
        num_Usuario = float(input('enter your number: '))

    else:
        print('The number you entered is correct!')
        verify = False
"""""

#ex 3
"""""
def sides():
    side1 = float(input('enter your side 1: '))
    side2 = float(input('enter your side 2: '))
    side3 = float(input('enter your side 3: '))

    types(side1, side2, side3)

def types(s1,s2,s3):
    if s1 != s2 and s1 != s3:
        print('Scalene')
    elif s1 == s2 and s1 != s3:
        print('Isoceles')
    elif s1 == s3 and s1 == s2:
        print('Equilateral')
    else:
        print(' Something went wrong try again')
        sides()

sides()
"""""

def sides():
    cont = 0
    side = ['','','']
    while cont < 3:
        side[cont] = float(input('enter your side: '))
        cont +=1
