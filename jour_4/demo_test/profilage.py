from operations import factorielle
import cProfile, pstats, io

pr = cProfile.Profile()
pr.enable()
result = factorielle(90000)
pr.disable()
s = io.StringIO()
ps = pstats.Stats(pr,stream=s).sort_stats("cumtime")
ps.print_stats(20)
print(s.getvalue())