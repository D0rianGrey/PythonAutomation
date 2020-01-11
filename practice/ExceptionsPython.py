ItemInCart = 0
# if ItemInCart != 2:
#     raise Exception("Products Cart count no matching")

assert (ItemInCart == 0)

try:
    with open('log.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print("It runs every time")
