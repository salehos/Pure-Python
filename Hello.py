print("Hello world")
one = 1
print(type(one))
float_one = 1.0
float_one = float_one + one
print(type(float_one))
list_1 = [1 , 2]
list_2 = [ 3 , 0 ]

print(list_1 + list_2)

list_sorted = list_1+list_2

print(sorted(list_sorted))
#sort kardane list

def func1(str1 , str2):
    #se ta ' ya " bzan baad ye enter bezan
    """
    :param str1:
    :param str2:
    :return:
    """
    str3 = "str1 is : %(str1)s , str2 is :%(str2)s" % ({
        "str1" : str1,
        "str2" : str2
    })

    str4 = "str1 is : %s , str2 is : %s" %(str1 , str2)

    print(str3)

    print("and for str 4 " + str4)

func1("golabi" , "sib")

float_1 = 10.123
integer_1 = "%d" %(float_1)
print(integer_1)