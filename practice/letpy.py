# default = input()
# default_with_out_space = default.replace(" ", "").lower()
# reverse = default_with_out_space[::-1].lower()
# if default_with_out_space == reverse:
#     print("Да")
# else:
#     print("Нет")
#     print(default_with_out_space)
#     print(reverse)


# a = input()
#
# if len(a) >= 8 and a.isdigit():
#     final = a.replace(a[0:-4], "*")
#     size = len(a) - 5
#     print("*" * size + final)
# else:
#     print("Ошибка")


a = input()
if "#" in a:
    print(a[:a.find("#")])
else:
    print("There isn't '#'")
    print(a)
