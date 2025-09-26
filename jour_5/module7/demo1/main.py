import ctypes

libc = ctypes.CDLL("msvcrt.dll")

libc.printf(b"Bonjour depuis c (Windows)\n")