'''
coefficitents: 3 -4 5 equals 3 -4x + 5x^2 and 2 0 0 5 = 2 + 5x^3
interval: 5 -5 equals interval (-5,5)
'''

def solve(coefficients, interval, resolution=10**-2, tolerance = 10**-6,threshold = 10**-3):
    interval = interval.split()
    start = float(interval[0])
    end = float(interval[-1])
    intervals = []      # breaks interval into multiple subintervals and searches each one. Does this so all changes in sign can be found
    roots = []
    # loop creates the subintervals with a range of variable resolution
    while True:
        if (start + resolution) < end:
            intervals.append([start, start + resolution])
            start = start + resolution
        else:
            intervals.append([start,end])
            break
    for points in intervals:
        a, b= float(points[0]), float(points[-1])
        a_val = eval(coefficients, a)       # value of polynomial when x = a
        b_val = eval(coefficients, b)       # value of polynomial when x = b
        
        a_der = eval_der(coefficients,a)    # derivative of polynomial when x = a
        b_der = eval_der(coefficients,b)    # derivative of polynomial when x = b

        # This checks if one point is positive and the other is negative
        if ((a_val > 0) and (b_val < 0)) or ((a_val < 0) and (b_val > 0)):
            n = 0
            # prevents infinite loop
            while n < 50:
                n +=1
                c = (a + b)/2
                c_val = eval(coefficients, c)
                # is true if function equal 0 at point c
                if (c_val == 0) or ((b-a)/2 < tolerance):
                    if c not in roots:
                        roots.append(round(c,5))
                        break
                # if point c and point a give same sign value, replace a with c
                if (c_val > 0 and a_val > 0) or (c_val < 0 and a_val < 0):
                    a = c
                # if point c and point b give same sign value, replace b with c
                elif (c_val > 0 and b_val > 0) or (c_val < 0 and b_val < 0):
                    b = c

        # This check if one point is positive and the other is negative in the derivative of the polynomial
        # This is to find points that touch 0 but never cross the x-axis
        elif ((a_der > 0) and (b_der < 0)) or ((a_der < 0) and (b_der > 0)):
            n = 0
            # prevents infinite loop
            while n < 50:
                n +=1
                c = (a + b)/2
                c_der = eval_der(coefficients, c)
                # is true if derivative equal 0 at point c
                if (c_der == 0) or ((b-a)/2 < tolerance):
                    # is true if function equal 0 as well at point c 
                    if abs(eval(coefficients,c)) < threshold: 
                        if c not in roots:
                            roots.append(round(c,5))
                            break
                # if point c and point a give same sign value, replace a with c
                if (c_der > 0 and a_der > 0) or (c_der < 0 and a_der < 0):
                    a = c
                # if point c and point b give same sign value, replace b with c
                elif (c_der > 0 and b_der > 0) or (c_der < 0 and b_der < 0):
                    b = c
    return roots

# This functions evaluates the value of a polynomial given an x value
def eval(coefficients, val):
    x = 0
    evaluation = 0
    for co in coefficients.split():
        evaluation += (val**x) * float(co)   #val ** x is the point multipled by degree of power and co is coefficient
        x += 1
    return evaluation

# This functions evaluates the derivative of a polynomial given a x value
def eval_der(coefficients, val):
    coefficients = coefficients.split()
    new_co = ""
    x = 0
    # get derivative of polynomial in new_co
    for co in coefficients:
        if x == 0:
            x += 1
            continue
        if co == 0:
            x += 1
            continue
        new_co += f'{x * float(co)} ' #power rule coefficient times the x (the degree of power)
        x += 1
    return eval(new_co, val)


if __name__ == '__main__':

    done = False
    while not done:
        coefficients = input('Enter the polynomial coefficients:\n') 
        interval = input('Enter the interval:\n')
        roots = solve(coefficients, interval)
        if roots:
            for root in roots:
                print(f'Root found at {root}.')    
        else:
            print('No roots are found!')
        answer = input('Do you want to continue? [Y/N]\n').upper()
        if answer != 'Y':
            done = True