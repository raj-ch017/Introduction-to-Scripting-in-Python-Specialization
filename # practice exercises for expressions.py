# practice exercises for expressions

# the exercise asks for writing the python statement
# which I will write under simple functions

def miles_to_feet(x):            # 1 mile = 5280 feet
    y = x * 5280
    print(str(x) + " miles in feet is:",y,"feet")

#miles_to_feet(10)

def hours_seconds(h,m,s):
    s1 = h * 3600
    s2 = m * 60
    total_secs = s + s1 + s2
    print(str(h),"hours",str(m),"minutes",str(s),"seconds is equal to",total_secs,"seconds in total.")

#hours_seconds(7,21,37)

def perimeter_rectangle(w,h):
    p = 2*w + 2*h
    print("A rectangle having",w,"units width and",h,"units height has a perimeter of",p,"units.")

#perimeter_rectangle(10,10)

def area_rectangle(w,h):
    a = w * h
    print("Area:",w,"units *",h,"units =",a,"square units")

#area_rectangle(12,13)

def circum_circle(r):
    pi = 3.14   
    c = 2 * pi * r
    print("The circumference of a circle with radius",r,"units is",c,"units")

#circum_circle(5)

def area_circle(r):
    pi = 3.14
    a = pi * (r**2)
    print("The area of a circle with radius",r,"units is",a,"square units")

#area_circle(5)

def interest_calc(p,r,t):
    # p stands for the principal amount
    # r represents rate of interest in percentage
    # t represents time period
    total = p * (1 + (0.01*r))**(t)
    print("Principal Amount:",p)
    print("Rate:",str(r) + "%")
    print("Time period:",t)
    print("Total amount:",total)

#interest_calc(1000,7,10)

def string_addition1():
    a = "My name is"
    b = "Rajdeep"
    c = "Chakraborty"
    d = "."
    print(a,b,c + d)

#string_addition1()

def string_addition2(y):
    a = "Rajdeep"
    b = "Charkraborty"
    c = "is"
    d = str(y) + " years old"
    e = "."
    print(a,b,c,d + e)

#string_addition2(22)

def dist_between_points(x1,y1,x2,y2):
    del_x = x2 - x1
    x = del_x ** 2
    del_y = y2 - y1
    y = del_y ** 2
    d = (x + y) ** (0.5)
    print("The distance between " + "(" + str(x1) + "," + str(y1) + ") " + "and " + "(" + str(x2) + "," + str(y2) + ") " + "is:",d,"units")

dist_between_points(2,2,5,6)
