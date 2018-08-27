import sys
def hello(a, b):
    add = a + b
    return add
x=hello(sys.argv[1], sys.argv[2])
print(x)