
x = input("Premier nombre:\n")
y = input("Deuxieme nombre:\n")
# if(float(y) == 0):
#     print("impossible la div sur zero")
#     exit()
try:
    result = float(x) / float(y)
    print(f"X / Y = {result}")
except ZeroDivisionError:
    print("impossible la div sur zero")