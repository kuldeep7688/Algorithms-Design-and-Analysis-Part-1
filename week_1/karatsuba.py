import math


def num_of_digits(num):
    "count the number of digits in the number"
    if num == 0:
        return int(1)

    num = abs(num)
    if num <= 999999999999997:
        return int(math.log10(num) + 1)

    count = 0
    while num:
        num //= 10
        count += 1
    return int(count)


def karatsuba_multiplication_algorithm(m, n):
    num_digits_m = num_of_digits(m)
    num_digits_n = num_of_digits(n)
    num_digits = max(num_digits_m, num_digits_n)
    num_digits_by_2 = math.floor(num_digits / 2)

    if num_digits == 1:
        return m * n
    else:
        a = (m // (10**num_digits_by_2))
        b = m - a*(10**num_digits_by_2)

        c = (n // (10**num_digits_by_2))
        d = n - c*(10**num_digits_by_2)

        one = karatsuba_multiplication_algorithm(a, c)
        two = karatsuba_multiplication_algorithm(b, d)
        three = karatsuba_multiplication_algorithm(a + b, c + d)
        four = three - two - one

        return (10**(num_digits_by_2*2))*one + (10**num_digits_by_2)*four + two


if __name__ == "__main__":
    num1 = 3141592653589793238462643383279502884197169399375105820974944592
    num2 = 2718281828459045235360287471352662497757247093699959574966967627
    print(int(karatsuba_multiplication_algorithm(num1, num2)))
    print(num1*num2)
