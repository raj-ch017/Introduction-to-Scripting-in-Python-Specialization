#quiz 2

def funct_calc(x):
    t1 = 5 * (x**5)
    t2 = 67 * (x**2)
    t3 = 47
    val = -t1 + t2 - t3
    print("The value of the function for input",x,"is:",val)

#funct_calc(3)

def future_value(present_value,annual_rate,periods_per_year,years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    val = present_value * (1+rate_per_period)**periods
    print("$"+str(present_value)+" invested at " + str(annual_rate) + "%" + " compounded daily for " + str(years) + " years yields $" + str(val))

future_value(1000,0.02,365,4)

def equilateral_area(side):
    c = (3**0.5)/4
    val = c * (side**2)
    print("An equilateral triangle with side length",side,"units is:",val,"square units")

#equilateral_area(5) 