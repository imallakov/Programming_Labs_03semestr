#538
import sys
import math

def main():
    nums = get_list()
    my_nums = get_my_nums(nums)
    try:
        geom_mean = geometric_mean(my_nums)
        minimum = min(my_nums)
        sorted_nums = sorted(nums[:math.ceil(len(nums)/3)])
    except ZeroDivisionError as error:
        sys.exit(str(error))
    print(f"geometric mean = {geom_mean}\nminimum number = {minimum}\nsorted numbers = {sorted_nums}")



def geometric_mean(nums):
    if len(nums)==0:
        raise ZeroDivisionError("В массиве не существует числа удовлетворяющие условию задачи")
    temp  = 1
    for num in nums:
        temp*=num

    n = len(nums)

    return temp**(1.0/n)



def get_my_nums(nums):
    my_nums = []
    for num in nums[:len(nums)//3]:
        if 4<=num<=20:
            my_nums.append(num)

    return my_nums



def get_list():
    nums = list(map(int, input().split()))

    return nums



if __name__ == "__main__":
    main()
