plus = lambda x,y: x+y
print(f"5 + 9 = {plus(5,9)}")

nums = [5,8,4,6,5,2,1,3]
print("nums",nums)

nums_pair = list(filter(lambda n: n % 2 == 0, nums))
print("nums_pair",nums_pair)