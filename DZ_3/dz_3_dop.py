from random import randint

polynomial={}
str_polinomials ={}

degree = int(input("введите максимальную степень многочлена: "))
degree2 = int(input("введите максимальную степень второго многочлена: "))
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


def str_sum_pol(pol):
    strin = ""
    for j in pol:
        if strin != '' and j[:1] != '-':
            strin += f' + {j}'
        else:
            strin += f' {j}'
    return strin

def sum_polynomial(polynomial):
    if (len(polynomial[1])) > (len(polynomial[2])):
        big = 1
        min = 2
    else:
        big = 2
        min = 1
    one = polynomial[big]
    two = polynomial[min]
    
    sums = []
    for count in range(len(one)):
        if count >= len(two):
            num2 = 0
            num1 = one[count]
        else:
            num1 = one[count]
            num2 = two[count]
        
        sum = num1 + num2
        sums.insert(0,sum)
    return sums

def str_polinomial(polinom, num_list):
    summ = polinom[num_list]
    str_pol = []
    for i in range(len(summ)):

        if summ[i] == 0:
            continue
        else:
            if i== 0:
                str_pol.insert(0,f'{summ[i]}')
            elif i == 1:
                str_pol.insert(0,f'{summ[i]}*x')
            else:
                str_pol.insert(0,f'{summ[i]}*x**{i}')
    return str_pol

polynomial[1]= new_polinomial(degree)
str_polinomials[1] = str_sum_pol(string)
string = []

polynomial[2]= new_polinomial(degree2)
str_polinomials[2] = str_sum_pol(string)

polynomial[3] = sum_polynomial(polynomial) 
str_polinomials[3] = str_sum_pol(str_polinomial(polynomial,3))
print(polynomial)
print(f"({str_polinomials[1]}) + ({str_polinomials[2]}) = ({str_polinomials[3]})")

