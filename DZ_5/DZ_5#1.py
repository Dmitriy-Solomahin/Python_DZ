# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def A_degree_B(number: int, degree: int) -> int:
    if degree == 1:
        return number
    elif degree == 0:
        return 1
    return A_degree_B(number, degree-1) * number


num_a = int(input("введите число а: "))
num_b = int(input('введите число б: '))

print(A_degree_B(num_a, num_b))

