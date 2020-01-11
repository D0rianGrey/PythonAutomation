#file = open('test.txt')


# print(file.read())
# print(file.readline())

# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

def read(path):
    file = open(path)
    print(file.read())
    file.close()


read('test.txt')

