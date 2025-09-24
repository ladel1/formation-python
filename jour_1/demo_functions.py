PI = 3.14
result = 0

def mult(x:float,y:float) -> float: # pure
    """
        Une fonction qui permet de multiplier deux nombres
    """
    return x * y

def calcul(x, y): # ce n'est pas une fonction pure
    """
        Une fonction qui permet de calculer surface d'un machin
    """    
    global result
    result = x / y * PI + result
    return result

print("********* mult *********")
print(mult(2,3))
print(mult(2,3))
print(mult(2,3))

print("********* calcul *********")
print(calcul(2,3))
print(calcul(2,3))
print(calcul(2,3))
print(calcul(2,3))