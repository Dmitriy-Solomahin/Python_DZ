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
    summ = polinom[3]
    for i in range(len(summ)):
        print(i)
        str_pol = []
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

polynomial[2]= new_polinomial(degree)
str_polinomials[2] = str_sum_pol(string)

polynomial[3] = sum_polynomial(polynomial) 
str_polinomials[3] = str_sum_pol(str_polinomial(polynomial))
print(polynomial)
print(f"({str_polinomials[1]}) + ({str_polinomials[2]}) = ({str_polinomials[3]})")

