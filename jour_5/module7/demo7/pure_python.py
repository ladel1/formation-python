"""
créer une fonction pure python
"""
import cProfile, pstats, io

def add_many(n):
    s = 0
    for i in range(n):
        # s = s + i
        s += i
    return s

pr = cProfile.Profile()
pr.enable()
# appeler la méthode créé en python pure
print(add_many(100000000))
pr.disable()

s = io.StringIO()

ps = pstats.Stats(pr, stream=s).sort_stats("cumtime")
ps.print_stats(20)
print(s.getvalue())