import ctypes

# charger notre lib 'mylib.so'
libc = ctypes.CDLL("./mylib.so")
# type de params
libc.add.argtypes = [ctypes.c_int, ctypes.c_int]
libc.add.restype = ctypes.c_int
# appeler notre fonction add
print(libc.add(5,6))
