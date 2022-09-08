num = (input("введите значение : "))
def count_sum_digits (x):
    result = 0
    for i in num:
        if i != ".":
            result = result + int(i)
    return (result)
print (count_sum_digits(num))
