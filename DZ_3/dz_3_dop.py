from random import randint

# polynomial={}
# str_polinomials ={}

# degree = int(input("введите максимальную степень многочлена: "))
# degree2 = int(input("введите максимальную степень второго многочлена: "))
# string = []
# def new_polinomial(degree):

#     polynomial = []
#     for i in range(degree+1):
#         koef = randint(-100,101)
#         polynomial.insert(0, koef)
#         if koef == 0:
#             continue
#         else:
#             if i== 0:
#                 string.insert(0,f'{koef}')
#             elif i == 1:
#                 string.insert(0,f'{koef}*x')
#             else:
#                 string.insert(0,f'{koef}*x**{i}')
#     return polynomial


# def str_sum_pol(pol):
#     strin = ""
#     for j in pol:
#         if strin != '' and j[:1] != '-':
#             strin += f' + {j}'
#         else:
#             strin += f' {j}'
#     return strin

# def sum_polynomial(polynomial):
#     if (len(polynomial[1])) > (len(polynomial[2])):
#         big = 1
#         min = 2
#     else:
#         big = 2
#         min = 1
#     one = polynomial[big]
#     two = polynomial[min]
    
#     sums = []
#     for count in range(len(one)):
#         if count >= len(two):
#             num2 = 0
#             num1 = one[count]
#         else:
#             num1 = one[count]
#             num2 = two[count]
        
#         sum = num1 + num2
#         sums.insert(0,sum)
#     return sums

# def str_polinomial(polinom, num_list):
#     summ = polinom[num_list]
#     str_pol = []
#     for i in range(len(summ)):

#         if summ[i] == 0:
#             continue
#         else:
#             if i== 0:
#                 str_pol.insert(0,f'{summ[i]}')
#             elif i == 1:
#                 str_pol.insert(0,f'{summ[i]}*x')
#             else:
#                 str_pol.insert(0,f'{summ[i]}*x**{i}')
#     return str_pol

# polynomial[1]= new_polinomial(degree)
# str_polinomials[1] = str_sum_pol(string)
# string = []

# polynomial[2]= new_polinomial(degree2)
# str_polinomials[2] = str_sum_pol(string)

# polynomial[3] = sum_polynomial(polynomial) 
# str_polinomials[3] = str_sum_pol(str_polinomial(polynomial,3))
# print(polynomial)
# print(f"({str_polinomials[1]}) + ({str_polinomials[2]}) = ({str_polinomials[3]})")

def create_equation() -> dict:
    degree = int(input('введите максимальную степень: '))
    equation = {}
    for n in range(degree, -1, -1):
        equation[n] = randint(-100,100)
    return equation

def dict_to_str(equation: dict) -> str:
    new_eq = ''
    for degree,koef in equation.items():
        if koef != 0:
            new_eq += f'{koef}*x**{degree} + '
    if new_eq.startswith('1') or new_eq.startswith('-1'):
        new_eq = new_eq.replace('1*', '')
    return new_eq.replace('+ -', '- '). \
                replace('x**1 ', 'x '). \
                replace('*x**0', ''). \
                replace(' 1*x', ' x')[:-2] + '=0'

def str_to_dict(equation: str) -> dict:
    new_eq = equation.replace(' ', '')[:-2]. \
        replace('+', ' ').replace('-', ' -'). \
        replace('*x ', '*x**1 ').replace(' x ', ' 1*x**1 '). \
        replace(' -x ', ' -1*x**1 ').split()
    new_dict_eq = {}
    for item in new_eq:
        if 'x**' in item:
            if item.startswith('x') or item.startswith('-x'):
                new_item = item.split('x**')
                new_dict_eq[int(new_item[1])] = -1 if new_item[0] == '-' else 1
            elif '*x**' in item:
                new_item = item.split('*x**')
                new_dict_eq[int(new_item[1])] = int(new_item[0])
        else:
            new_dict_eq[0] = int(item)
    return new_dict_eq

def summ_dict(first: dict, second: dict) -> dict:
    final_dict = {}
    final_dict.update(first)
    final_dict.update(second)
    for degree in final_dict:
        final_dict[degree] = first.get(degree, 0) + second.get(degree, 0)
    return final_dict

dict_eq_1 = create_equation()
dict_eq_2 = create_equation()

final = summ_dict(dict_eq_1, dict_eq_2)

print(dict_to_str(dict_eq_1))
print(dict_to_str(dict_eq_2))
print(dict_to_str(final))
