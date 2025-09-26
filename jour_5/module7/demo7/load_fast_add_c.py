"""
Comparer entre une fonction créé en langage c avec une fonction python pure
"""
import ctypes
import cProfile, pstats, io

libc = ctypes.CDLL("./fast_add.dll")
libc.add_many.argtypes = [ctypes.c_int]
libc.add_many.restype = ctypes.c_int


pr = cProfile.Profile()
pr.enable()
# appeler la méthode créé et compilé en langage c
print(libc.add_many(100000000))
pr.disable()

s = io.StringIO()

ps = pstats.Stats(pr, stream=s).sort_stats("cumtime")
ps.print_stats(20)
print(s.getvalue())