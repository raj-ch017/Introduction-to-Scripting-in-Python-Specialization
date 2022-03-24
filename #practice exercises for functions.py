#practice exercises for functions

def triangle_area(x0,y0,x1,y1,x2,y2):
    #side length 1
    a = ((x1-x0)**2 + (y1-y0)**2 ) ** 0.5
    #side length 2
    b = ((x2-x1)**2 + (y2-y1)**2 ) ** 0.5
    #side length 3
    c = ((x2-x0)**2 + (y2-y0)**2 ) ** 0.5
    s = (a+b+c)/2
    area = ((s-a)*(s-b)*(s-c)*s) ** 0.5
    print("The area of the triangle with side lengths",a,"units,",b,"units and",c,"units are:",area)

#triangle_area(10,0,0,0,0,10)

def print_digits(i):
    #printing the digits of an integer between 0 and 99
    ones = i % 10
    num = i - ones
    tens = num // 10
    print("The tens digit is",str(tens)+", and the ones digit is",str(ones)+".")

#print_digits(3)

import random
def powerball():
    a = random.randrange(1,60)
    b = random.randrange(1,60)
    c = random.randrange(1,60)
    d = random.randrange(1,60)
    e = random.randrange(1,60)
    pn = random.randrange(1,36)

    print("Today's numbers are",str(a)+", "+ str(b) + ", " + str(c) + ", " + str(d) +" and "+str(e)+". The Powerball number is",str(pn)+".")

#powerball()