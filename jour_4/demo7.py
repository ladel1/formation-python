"""
    Module 5 pour utiliser docstring
"""

def mult(a:int, b:int) -> int:
    """
        une fonction qui permet de faire la multiplicaiton entre deux nombres
    """
    return a * b

def add(a:int, b:int) -> int:
    """
        une fonction qui permet de faire l'addition entre deux nombres
        <ul>
            <li>aaaa</li>
            <li>aaaa</li>
            <li>aaaa</li>
        </ul>
        <a href="https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/missing-final-newline.html">site internet</a>      
    """
    return a + b


add()