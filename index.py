n = int(input("Enter any number: "))


def sum_of_digits(num):
    s = 0
    while num > 0:
        s += num % 10
        num = num // 10
    return s


print(sum_of_digits(n))
