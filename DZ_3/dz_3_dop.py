from random import randint

polynomial={}
str_polinomials ={}

degree = int(input("введите максимальную степень многочлена: "))
string = []
def new_polinomial(degree):

    polynomial = []
    for i in range(degree+1):
        koef = randint(-100,101)
        polynomial.insert(0, koef)
        if koef == 0:
            continue
        else:
            if i== 0:
                string.insert(0,f'{koef}')
            elif i == 1:
                string.insert(0,f'{koef}*x')
            else:
                string.insert(0,f'{koef}*x**{i}')
    return polynomial

# def str_polinomial(polinom):
    i=0
    while i < len(polinom):
        str_pol = []
        if polinom[i] == 0:
            i+=1
            continue
        else:
            if i== 0:
                str_pol.insert(0,f'{polinom[i]}')
            elif i == 1:
                str_pol.insert(0,f'{polinom[i]}*x')
            else:
                str_pol.insert(0,f'{polinom[i]}*x**{i}')
        i +=1
    print(str_pol)
    return str_pol

def str_sum_pol(pol):
    strin = ""
    for j in pol:
        if strin != '' and j[:1] != '-':
            strin += f' + {j}'
        else:
            strin += f' {j}'
    return strin

def sum_polynomial(polynomial):
    one = polynomial[1]
    two = polynomial[2]
    
    sums = []
    for count in range(len(polynomial[1])):
        sum = one[count] + two[count]
        sums.append(sum)
        count+=1
    return sums

def str_polinomial(polinom):
    i=0
    while i < len(polinom):
        str_pol = []
        if polinom[i] == 0:
            i+=1
            continue
        else:
            if i== 0:
                str_pol.insert(0,f'{polinom[i]}')
            elif i == 1:
                str_pol.insert(0,f'{polinom[i]}*x')
            else:
                str_pol.insert(0,f'{polinom[i]}*x**{i}')
        i +=1
    print(str_pol)
    return str_pol

polynomial[1]= new_polinomial(degree)
str_polinomials[1] = str_sum_pol(string)
string = []
polynomial[2]= new_polinomial(degree)
str_polinomials[2] = str_sum_pol(string)

polynomial[sum] = sum_polynomial(polynomial) 



str_polinomials[sum] = str_sum_pol(str_polinomial(polynomial[sum]))
print(polynomial)
print(f"({str_polinomials[1]}) + ({str_polinomials[2]}) = ({str_polinomials[sum]})")

