import ctypes
import math
# chargement de librairie du langage c
libc = ctypes.CDLL("msvcrt.dll")
# typage de parameteres
libc.cos.argtypes = [ctypes.c_double]
libc.cos.restype = ctypes.c_double
# appel de la fonction cos de la librairie c msvcrt.dll
print(libc.cos(math.pi/3))