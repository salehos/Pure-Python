print("Hello world")
one = 1
print(type(one))
float_one = 1.0
float_one = float_one + one
print(type(float_one))
list_1 = [1, 2]
list_2 = [3, 0]

print(list_1 + list_2)

list_sorted = list_1 + list_2

print(sorted(list_sorted))


# sort kardane list

def func1(str1, str2):
    # se ta ' ya " bzan baad ye enter bezan
    """
    :param str1:
    :param str2:
    :return:
    """
    str3 = "str1 is : %(str1)s , str2 is :%(str2)s" % ({
        "str1": str1,
        "str2": str2
    })

    print(str3)

    str3 = str3.replace("str1", "string1")

    print(str3)

    str3 = str3.split(" ")

    print(str3)
    print(type(str3))

    for st in str3:
        if st == "is":
            continue;
        print(st)
    print("\n")

    for index, st in enumerate(str3):
        if st == "is":
            continue
        print(index, st)
    print("\n")
    str4 = "str1 is : %s , str2 is : %s" % (str1, str2)

    print("and for str 4 " + str4 + "\n")


func1("golabi", "sib")
dict1 = {
    "key1": "val1",
    "key2": "val2"
}

for key, value in dict1.items():
    print(key, value)

integer_1 = 10
float_1 = "%0.2f" % integer_1
print(float_1)
float2 = 4 / 3
print("%0.2f", float2)
import math


def func2(string1, string2):
    stringsum = string1 + string2
    print(stringsum)
    for s in stringsum:
        if 'a' in s:
            stringsum = stringsum.replace('a', 's')
    print(stringsum)
    print(stringsum[-4:])


func2("salam", "doostan")

list1 = [1, 2]
list2 = [1, 2]
if list1 == list2:
    print("list1 == list2")
if list1 is list2:
    print("list1 == list2")
print("\n")
for l in list1:
    print(l)
else:
    print("golabi")
# vaghti for ejra nashe else ejra mishe
print(len(list1))
for i in range(0, 10):
    print(i)
print("\n")
i = 0
while i < 5:
    print(i + 1)
    i += 1
print("\n")

def func3(str1=0 , str2 = "salam"):
    pass
