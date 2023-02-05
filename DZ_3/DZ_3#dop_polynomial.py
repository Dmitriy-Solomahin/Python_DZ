from random import randint

polynomial={}
str_polinomials ={}

degree = int(input("введите максимальную степень многочлена: "))

def new_polinomial(degree):
    polynomial = []
    for _ in range(degree+1):
        koef = randint(-100,101)
        polynomial.insert(0, koef)
    return polynomial

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
    count = 0
    sums = []
    while count< len(polynomial[1]):
        sum = one[count] + two[count]
        sums.append(sum)
        count+=1
    return sums

polynomial[1]= new_polinomial(degree)
polynomial[2]= new_polinomial(degree)

polynomial[sum] = sum_polynomial(polynomial) 

str_polinomials[1] = str_sum_pol(str_polinomial(polynomial[1]))
str_polinomials[2] = str_sum_pol(str_polinomial(polynomial[2]))
str_polinomials[sum] = str_sum_pol(str_polinomial(polynomial[sum]))
print(polynomial)
print(f"({str_polinomials[1]}) + ({str_polinomials[2]}) = ({str_polinomials[sum]})")