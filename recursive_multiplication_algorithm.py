import math

def recursive_multiplication_algorithm(num1, num2):
    num1_digits = num_of_digits(num1)
    num2_digits = num_of_digits(num2)
    # print(num1, num2)

    # base case
    if num1_digits <= 2 or num2_digits <= 2:
        return num1*num2
    else:
        a = (num1 // (10**math.floor(num1_digits/2.0)))
        b = num1 - a*(10**math.floor(num1_digits/2.0))

        c = (num2 // (10**math.floor(num2_digits/2.0)))
        d = num2 - c*(10**math.floor(num2_digits/2.0))
        print(a, b, c, d)

        result = (10**(math.floor(num1_digits/2.0) +\
                       math.floor(num2_digits/2.0)))*recursive_multiplication_algorithm(a, c) +\
                 (recursive_multiplication_algorithm(b, d)) +\
                 (10**math.floor(num1_digits/2.0))*recursive_multiplication_algorithm(a, d) +\
                 (10**math.floor(num2_digits/2.0))*recursive_multiplication_algorithm(b, c)

        return result


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


if __name__ == "__main__":
    num1 = 3141592653589793238462643383279502884197169399375105820974944592
    num2 = 2718281828459045235360287471352662497757247093699959574966967627
    print(int(recursive_multiplication_algorithm(num1, num2)))
    print(num1*num2)
