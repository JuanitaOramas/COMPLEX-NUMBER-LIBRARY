#Autor Juanita Oramas

# COMPLEX NUMBER LIBRARY
import math

#SUM
def sumacplx(a, b):
    real = a[0] + b[0]
    img = a[1] + b[1]
    if img >= 0:
        return str(real) + "+" + str(img) + "i"
    else:
        return str(real) + str(img) + "i"

#PRODUCT
def multicplx(a, b):
    real = (a[0] * b[0])-(a[1] * b[1])
    img = (a[0] * b[1])+(a[1] * b[0])
    if img >= 0:
        return str(real) + "+" + str(img) + "i"
    else:
        return str(real) + str(img) + "i"

#SUBSTRACTION
def restacplx(a, b):
    real = a[0] - b[0]
    img = a[1] - b[1]
    if img >= 0:
        return str(real) + "+" + str(img) + "i"
    else:
        return str(real) + str(img) + "i"

#DIVISION
def divicplx(a, b):
    real = ((a[0] * b[0])+(a[1] * b[1])) / ((b[0])**2 + (b[1])**2)
    img = ((b[0] * a[1])-(a[0] * b[1])) / ((b[0])**2 + (b[1])**2) #check
    a = (round(real,2 ), round(img,2 ))
    return str(a[0]) + str(a[1]) + "i"

#MODULE
def modulo (a):
    real = a[0]**2
    img = a[1]**2
    b= ((real + img)**0.5)
    return str(b)

#CONJUGATE
def conjugadoplx(a):
    real = a[0]
    img = a[1] * -1

    if img >= 0:
        return str(real) + "+" + str(img) + "i"
    else:
        return str(real) + str(img) + "i"

#POLAR AND CARTESIAN CONVERSION
def polarComp(a,b):
    r = math.sqrt(a*2 + b*2)
    angle = math.atan2(b,a)

    return (round(r, 2),round(angle, 2))


#COMPLEX NUMBER PHASE
def faseComp(a,b):
    angulo = math.atan2(a,b)
    return round(angulo, 3)


if __name__ == '__main__':
    print(sumacplx((2, 3), (4, 7)))
    print(restacplx((2, 3), (4, 7)))
    print(multicplx((2, 3), (4, 7)))
    print(divicplx((2, 3), (4, 7)))
    print(modulo((1, -1)))
    print(conjugadoplx((2, 3)))
    print(polarComp(2,3))
    print(faseComp(8,1))
